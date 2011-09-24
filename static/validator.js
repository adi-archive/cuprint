function validate_print_form(form){
	var unire = new RegExp('\\w{2,3}\\d{1,4}');
	
	if(!unire.test(form.uni.value)){
		alert('Please enter a valid UNI.');
		return false;
	}

	var filere = new RegExp('\\.(pdf)|(ps)|(doc)|(odt)|(docx)');

	if(!filere.test(form.document.value)){
		alert("Please upload a PDF or PostScript file.");
		return false;
	}

	if(!form.copies.value){
		alert("Please specify the number of copes.");
		return false;
	}

	var pagesre = new RegExp('[\d,-]*');

	if(!pagesre.test(form.pages.value)){
		alert("Please enter a page range in the form of 1,3-4 or leave blank.");
		return false;
	}

	return true;
}
