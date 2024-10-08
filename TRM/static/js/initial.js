(function ($) {

    var unicode_charAt = function(string, index) {
        var first = string.charCodeAt(index);
        var second;
        if (first >= 0xD800 && first <= 0xDBFF && string.length > index + 1) {
            second = string.charCodeAt(index + 1);
            if (second >= 0xDC00 && second <= 0xDFFF) {
                return string.substring(index, index + 2);
            }
        }
        return string[index];
    };

    var unicode_slice = function(string, start, end) {
        string = string.trim();
        var accumulator = "";
        var character;
        var stringIndex = 0;
        var unicodeIndex = 0;
        var length = string.length;
        var arr = string.split(' ');
        var first=true;
        if(end ==1){
            accumulator = unicode_charAt(string, stringIndex).toUpperCase();
        }
        else if(end==2 && arr.length>=2){
            accumulator = unicode_charAt(arr[0],0).toUpperCase() + unicode_charAt(arr[arr.length-1],0).toUpperCase();
        }
        else {
            while (stringIndex < length) {
                character = unicode_charAt(string, stringIndex);
                if (character == " "){
                    first=true;
                    continue;
                }
                if (unicodeIndex >= start && unicodeIndex < end) {
                    if (first){
                        character = character.toUpperCase();
                        first=false;
                    }
                    accumulator += character.toLowerCase();

                }
                stringIndex += character.length;
                unicodeIndex += 1;
            }
        }
        return accumulator;
    };

    $.fn.initial = function (options) {

        // Defining Colors
        var colors = ["#1abc9c", "#16a085", "#f1c40f", "#f39c12", "#2ecc71", "#27ae60", "#e67e22", "#d35400", "#3498db", "#2980b9", "#e74c3c", "#c0392b", "#9b59b6", "#8e44ad", "#bdc3c7", "#34495e", "#2c3e50", "#95a5a6", "#7f8c8d", "#ec87bf", "#d870ad", "#f69785", "#9ba37e", "#b49255", "#b49255", "#a94136"];

        return this.each(function () {

            var e = $(this);
            var settings = $.extend({
                // Default settings
                name: 'Name',
                seed: 0,
                charCount: 2,
                textColor: '#ffffff',
                height: 100,
                width: 100,
                fontSize: 40,
                fontWeight: 400,
                fontFamily: 'HelveticaNeue-Light,Helvetica Neue Light,Helvetica Neue,Helvetica, Arial,Lucida Grande, sans-serif',
                radius: 0
            }, options);

            // overriding from data attributes
            settings = $.extend(settings, e.data());

            // making the text object
            var c = unicode_slice(settings.name, 0, settings.charCount);
            var cobj = $('<text text-anchor="middle"></text>').attr({
                'y': '50%',
                'x': '50%',
                'dy' : '0.35em',
                'pointer-events':'auto',
                'fill': settings.textColor,
                'font-family': settings.fontFamily
            }).html(c).css({
                'font-weight': settings.fontWeight,
                'font-size': settings.fontSize+'px',
            });

            var colorIndex = Math.floor((c.charCodeAt(0) + settings.seed) % colors.length);

            var svg = $('<svg></svg>').attr({
                'xmlns': 'http://www.w3.org/2000/svg',
                'pointer-events':'none',
                'width': settings.width,
                'height': settings.height
            }).css({
                'background-color': colors[colorIndex],
                'width': settings.width+'px',
                'height': settings.height+'px',
                'border-radius': settings.radius+'px',
                '-moz-border-radius': settings.radius+'px'
            });

            svg.append(cobj);
           // svg.append(group);
            var svgHtml = window.btoa(unescape(encodeURIComponent($('<div>').append(svg.clone()).html())));

            e.attr("src", 'data:image/svg+xml;base64,' + svgHtml);

        })
    };

}(jQuery));
