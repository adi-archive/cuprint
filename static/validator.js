var cuprint = {};

cuprint.validate_print_form = function() {
	//individual functions
	//inline errors, in order
	var unire = /\\w{2,3}\\d{1,4}/;
	if (!unire.test(this.uni.value)) {
		cuprint.show_error('Please enter a valid UNI.');
		return false;
	}

	var filere = /\\.(pdf)|(ps)/;
	if (!filere.test(this.document.value)) {
		cuprint.show_error("Please upload a PDF or PostScript file.");
		return false;
	}

	if (!this.copies.value) {
		cuprint.show_error("Please specify the number of copes.");
		return false;
	}

	var pagesre = /[\d,-]*/;
	if (!pagesre.test(this.pages.value)) {
		cuprint.show_error("Please enter a page range in the form of 1,3-4 or leave blank.");
		return false;
	}

	return true;
}

cuprint.show_error = function(msg) {
	alert(msg);
}

// Shorthand for $(document).ready(func);
$(function() {
	$('#print_form').submit(cuprint.validate_print_form);
});
