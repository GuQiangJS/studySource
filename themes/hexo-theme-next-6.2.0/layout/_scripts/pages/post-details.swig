<script type="text/javascript" src="{{ url_for(theme.js) }}/src/scrollspy.js?v={{ theme.version }}"></script>
<script type="text/javascript" src="{{ url_for(theme.js) }}/src/post-details.js?v={{ theme.version }}"></script>


	
	<style type="text/css">
	  .no-before::before {
		content: "";
		padding: 0px;
	  }
	  .no-before{
	  font-weight: bold;
	  font-style: normal;
	  }
	  </style>
	<script type="text/javascript">
	$("cite").each(function(index){
		if($(this).prev().length==0 && $(this)[0].children.length==1)
		{
			$(this)[0].className='no-before';
		}
	});
	</script> 