var cuprint = {};

cuprint.validate_print_form = function() {
	//individual functions
	//inline errors, in order
	var unire = /\w{2,3}\d{1,4}/;
	if (!this.uni.value.match(unire)) {
		cuprint.show_uni_error();
		return false;
	}

	var filere = /\.(pdf)|(ps)/;
	if (!this.document.value.match(filere)) {
		cuprint.show_document_error();
		return false;
	}

	if (!this.copies.value) {
		cuprint.show_copies_error();
		return false;
	}

	var pagesre = /[\d,-]*/;
	if (!this.pages.value.match(pagesre)) {
		cuprint.show_pages_error();
		return false;
	}

	return true;
}

cuprint.show_uni_error = function() {
	$('#uni').after('<span class="error">Please enter a valid UNI.</span>');
}

cuprint.show_document_error = function() {
	$('#document').after('<span class="error">Please upload a PDF or PostScript file.</span>');
}

cuprint.show_copies_error = function() {
	$('#copies').after('<span class="error">Please specify the number of copies.</span>');
}

cuprint.show_pages_error = function() {
	$('#pages').after('<span class="error">Please enter a page range in the form of 1,3-4 or leave blank.</span>');
}

// Shorthand for $(document).ready(func);
$(function() {
	$('#print_form').submit(cuprint.validate_print_form);
});
