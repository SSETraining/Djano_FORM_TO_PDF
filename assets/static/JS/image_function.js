function get_images(image,descrip){
    const image_list = []
    const image_description=[]
    let count=0
    list=document.querySelectorAll(image)
    description=document.querySelectorAll(descrip)
    for (let i  in list){
        if(list[i].files.lenght==0){}
        else{
            image_list[count]=list[i].files[0];
            image_description[count]=description[i].value;
            count=count+1;
        }
    }
    return {"image_list":image_list},{"image_description":image_description}
}