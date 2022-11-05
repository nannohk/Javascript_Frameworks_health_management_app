// import validations from "./validations";

export default class signInCalidations{
    constructor(email, password){
        this.email = email;
        this.password = password;
    }

    checkEmail(){
        let emailErr = "";
        //email validation
        if(this.email != "test@gmail.ca"){
           emailErr = "Invalid email";
        }
        return emailErr;
    }
       
    //password validation
    checkPassword(){
        let passwordErr = "";
    if(this.password != 'test'){
            passwordErr = "Password is incorrect";
        }
        return passwordErr;
    }
  
}