console.log("enter in the pdffile")
$(document).ready(function() {
    function getCookie(name) {
          let cookieValue = null;
          if (document.cookie && document.cookie !== '') {
              const cookies = document.cookie.split(';');
              for (let i = 0; i < cookies.length; i++) {
                  const cookie = cookies[i].trim();
                  // Does this cookie string begin with the name we want?
                  if (cookie.substring(0, name.length + 1) === (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');
        /* ... */
        /* send a POST request to create a todo */
        $('#createPdfButton').click(function(e) {
        e.preventDefault(); // prevent the page from reload
        let myFormData = new FormData();
        let Builder=document.querySelector('#Builder').value
        let Community=document.querySelector('#Community').value
        let Q_Notes=document.querySelector('#Q_Notes').value
        let S_Notes=document.querySelector('#S_Notes').value
        let H_Notes=document.querySelector('#H_Notes').value
        let F_Notes=document.querySelector('#F_Notes').value
        let Summary_Notes= document.querySelector("#paragraphInputfinal").value
        let dict_Question=Fetch_data('#Question_Class', '#Question_label')
        let dict_Home=Fetch_data('#Home_Class', '#Home_label')
        let dict_sales=Fetch_data('#sales_class', '#Sales_label')
        let dict_inventory=Fetch_data('#inventory_class', '#Inventory_label')
        let image_list_F=get_images('#imageFile_F','#imageDescription_F');
        let image_list_Q=get_images('#imageFile_Q','#imageDescription_Q');
        let image_list_S=get_images('#imageFile_S','#imageDesimageDescription_Hcription_S');
        let image_list_H=get_images('#imageFile_H','#imageDescription_H');
        myFormData.append('Builder',Builder)
        myFormData.append('Community',Community)
        myFormData.append('Q_Notes',Q_Notes)
        myFormData.append('S_Notes',S_Notes)
        myFormData.append('H_Notes',H_Notes)
        myFormData.append('F_Notes',F_Notes)
        myFormData.append('Summary_Notes',Summary_Notes)
        myFormData.append('Question',JSON.stringify(dict_Question))
        myFormData.append('Home',JSON.stringify(dict_Home))
        myFormData.append('sales',JSON.stringify(dict_sales))
        myFormData.append('inventory',JSON.stringify(dict_inventory))
        myFormData.append('image_list_F',JSON.stringify(image_list_F))
        myFormData.append('image_list_H',JSON.stringify(image_list_H))
        myFormData.append('image_list_Q',JSON.stringify(image_list_Q))
        myFormData.append('image_list_S',JSON.stringify(image_list_S))
        let imge_Q_link=return_images_ids('imageFile_Q',7)
        for(let i=0;i<imge_Q_link.length;i++){
          console.log("dsasds",imge_Q_link[i])
          myFormData.append(imge_Q_link[i],document.getElementById(imge_Q_link[i]).files[0])
        }
        myFormData.append('images',document.getElementById('imageFile_Q1').files[0])
        let url = "PDF_FILE"
        console.log("Form_Data",myFormData)
          $.ajax({
            url: url,
            type: 'POST',
            data: myFormData,
            processData: false,
            contentType: false,
            // contentType: 'multipart/form-data',
          }).done(function(response) {
            document.getElementById("uploadForm").reset();
              console.log("log",response) // let's just print the data in the console for now
            })
          $(this).trigger('reset') // reset the form
        })
      })