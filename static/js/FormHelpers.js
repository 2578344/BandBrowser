function getFormData(formID){
    var formData = {};
    $(formID).find("input, textarea, select").each(function(index, element){
        formData[element.name] = element.value;
    });
    return formData;
}

function validateFormData(formData){
    for(var key in formData){
        if(formData[key] == "" ){
            const res = {
                status: false,
                message: "Please fill out all fields"
            }
            return res;
        }
    }
    return { status: true, message: "Form is valid" };
}
