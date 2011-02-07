<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(w.attrs)} class='column' style="width: ${w.attrs['width']};">
% for entry in w.children:
	${entry.display() | n }
% endfor
</div>
