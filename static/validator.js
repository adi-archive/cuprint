function validate_print_form(form){
	var unire = new RegExp('\\w{2,3}\\d{1,4}');
	
	if(!unire.test(form.uni.value)){
		alert('Invalid UNI');
		return false;
	}

	var filere = new RegExp('\\.(pdf)|(ps)');

	if(!filere.test(form.document.value)){
		alert("Invalid file type. Only PDF and PostScript files are accepted at this time.");
		return false;
	}

	if(!form.copies.value){
		alert("Must specify number of copies.");
		return false;
	}

	var pagesre = new RegExp('[\d,-]*');

	if(!pagesre.test(form.pages.value)){
		alert("Invalid page range. Must be in the form of 1,3-4 or left blank");
		return false;
	}

	return true;
}
