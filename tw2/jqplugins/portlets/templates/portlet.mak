<%namespace name="tw" module="tw2.core.mako_util"/>
<div ${tw.attrs(w.attrs)} class='portlet'>
  <div class='portlet-header'>${w.title}</div>
  <div class='portlet-content'>
  % if hasattr(w, 'children'):
  % for child in w.children:
      ${child.display() | n}<br/>
  % endfor
  % endif
  </div>
</div>
