import sublime, sublime_plugin
#view.run_command("html_encode")

class HtmlEncodeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
    	html_codes = {' ': '&nbsp;','<':'&lt;','>':'&gt;'} #code database
    	
    	for code in html_codes: #
    	
	        for region in self.view.sel():  #get region that is highlighted

	            if not region.empty():  #ensure that we have contents to work with
	                 
	                s = self.view.substr(region)  #get the string of region we are viewing
	                
	                s = s.replace(code,html_codes[code])  
	                 
	                self.view.replace(edit,region, s)

	    #convert all escape characters to <br/> tagg.
	    #we do this last so we dont try to convert this code to html encoding. 
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                s = s.replace('\n','<br/>\n')
                self.view.replace(edit,region,s)