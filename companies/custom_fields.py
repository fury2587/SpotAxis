# -*- coding: utf-8 -*-
"""
Mexican-specific form helpers.
"""
from __future__ import unicode_literals
import re

from django.forms import ValidationError
from django.forms.fields import RegexField, CharField
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EMPTY_VALUES

DATE_RE = r'\d{2}((01|03|05|07|08|10|12)(0[1-9]|[12]\d|3[01])|02(0[1-9]|[12]\d)|(04|06|09|11)(0[1-9]|[12]\d|30))'

#: This is the list of inconvenient words according to the `Anexo IV` of the
#: document described in the next link:
#: http://www.sisi.org.mx/jspsi/documentos/2005/seguimiento/06101/0610100162005_065.doc
RFC_INCONVENIENT_WORDS = [
    'BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO',
    'COGE', 'COJA', 'COJE', 'COJI', 'COJO', 'CULO', 'FETO', 'GUEY',
    'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 'KOGE', 'KOJO', 'KAKA',
    'KULO', 'MAME', 'MAMO', 'MEAR', 'MEAS', 'MEON', 'MION', 'MOCO',
    'MULA', 'PEDA', 'PEDO', 'PENE', 'PUTA', 'PUTO', 'QULO', 'RATA',
    'RUIN',
]


class MXRFCField_Custom(RegexField, CharField):
    """
    A form field that validates a Mexican *Registro Federal de Contribuyentes*
    for either `Persona física` or `Persona moral`.

    The Persona física RFC string is integrated by a juxtaposition of
    characters following the next pattern:

        =====  ======  ===========================================
        Index  Format  Accepted Characters
        =====  ======  ===========================================
        1      X       Any letter
        2      X       Any vowel
        3-4    XX      Any letter
        5-10   YYMMDD  Any valid date
        11-12  XX      Any letter or number between 0 and 9
        13     X       Any digit between 0 and 9 or the letter *A*
        =====  ======  ===========================================

    The Persona moral RFC string is integrated by a juxtaposition of
    characters following the next pattern:

        =====  ======  ============================================
        Index  Format  Accepted Characters
        =====  ======  ============================================
        1-3    XXX     Any letter including *&* and *Ñ* chars
        4-9    YYMMDD  Any valid date
        10-11  XX      Any letter or number between 0 and 9
        12     X       Any number between 0 and 9 or the letter *A*
        =====  ======  ============================================

    More info about this:
        http://es.wikipedia.org/wiki/Registro_Federal_de_Contribuyentes_(M%C3%A9xico)
    """
    default_error_messages = {
        'invalid': _(u'Ingrese un RFC válido'),
        'invalid_checksum': _(u'Suma de verificación inválida'),
        'required': _(u'Ingrese el RFC de la empresa'),
    }

    def __init__(self, min_length=9, max_length=13, *args, **kwargs):
        rfc_re = re.compile(r'^([A-Z&Ññ]{3}|[A-Z][AEIOU][A-Z]{2})%s([A-Z0-9]{2}[0-9A])?$' % DATE_RE,
                            re.IGNORECASE)
        super(MXRFCField_Custom, self).__init__(rfc_re, min_length=min_length,
                                         max_length=max_length, *args, **kwargs)

    def clean(self, value):
        value = super(MXRFCField_Custom, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = value.upper()
        if self._has_homoclave(value):
            if not value[-1] == self._checksum(value[:-1]):
                raise ValidationError(self.default_error_messages['invalid_checksum'])
        if self._has_inconvenient_word(value):
            raise ValidationError(self.default_error_messages['invalid'])
        return value

    def _has_homoclave(self, rfc):
        """
        This check is done due to the existance of RFCs without a *homoclave*
        since the current algorithm to calculate it had not been created for
        the first RFCs ever in Mexico.
        """
        rfc_without_homoclave_re = re.compile(r'^[A-Z&Ññ]{3,4}%s$' % DATE_RE,
                                              re.IGNORECASE)
        return not rfc_without_homoclave_re.match(rfc)

    def _checksum(self, rfc):
        """
        More info about this procedure:
            www.sisi.org.mx/jspsi/documentos/2005/seguimiento/06101/0610100162005_065.doc
        """
        chars = '0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ-Ñ'
        if len(rfc) == 11:
            rfc = '-' + rfc

        sum_ = sum(i * chars.index(c)
                   for i, c in zip(reversed(range(14)), rfc))
        checksum = 11 - sum_ % 11

        if checksum == 10:
            return 'A'
        elif checksum == 11:
            return '0'

        return six.text_type(checksum)

    def _has_inconvenient_word(self, rfc):
        first_four = rfc[:4]
        return first_four in RFC_INCONVENIENT_WORDS