function pdf_file()
{
console.log("Enter in the JS File")
const docElement = document.getElementById('uploadForm');
html2pdf().from(docElement).save('filename.pdf');
}