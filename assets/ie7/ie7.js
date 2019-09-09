/* To avoid CSS expressions while still supporting IE 7 and IE 6, use this script */
/* The script tag referencing this file must be placed before the ending body tag. */

/* Use conditional comments in order to target IE 7 and older:
	<!--[if lt IE 8]><!-->
	<script src="ie7/ie7.js"></script>
	<!--<![endif]-->
*/

(function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'lmms\'">' + entity + '</span>' + html;
	}
	var icons = {
		'lmms-lmms-export': '&#xe900;',
		'lmms-lmms-ticket': '&#xe901;',
		'lmms-lmms-attachment': '&#xe902;',
		'lmms-lmms-lab': '&#xe903;',
		'lmms-lmms-true': '&#xe904;',
		'lmms-lmms-false': '&#xe905;',
		'lmms-lmms-task': '&#xe906;',
		'lmms-lmms-arrow': '&#xe907;',
		'lmms-lmms-settings': '&#xe908;',
		'lmms-lmms-logout': '&#xe909;',
		'lmms-lmms-notification': '&#xe90a;',
		'lmms-lmms-list-normal': '&#xe90b;',
		'lmms-lmms-list-hover': '&#xe90c;',
		'0': 0
		},
		els = document.getElementsByTagName('*'),
		i, c, el;
	for (i = 0; ; i += 1) {
		el = els[i];
		if(!el) {
			break;
		}
		c = el.className;
		c = c.match(/lmms-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
}());
