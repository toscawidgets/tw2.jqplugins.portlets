<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
<div ${tw.attrs(w.attrs)} class='portlet'>
  <div class='portlet-header'>${w.title}</div>
  <div class='portlet-content'>${w.content}</div>
</div>
<script type="text/javascript">
makeIntoPortlet('${w.attrs["id"]}');
</script>
</div>
