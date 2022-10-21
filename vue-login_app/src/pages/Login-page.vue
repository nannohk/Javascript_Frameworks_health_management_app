<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
            <div>
            <h3>Login</h3>
            <hr/>
        </div>
        <form>
            <div class="form-group">
                <label>Email</label>
                <input type="email" class="form-control" placeholder="Enter email" v-model="email" >
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control" placeholder="Enter password" v-model="password" >
            </div>

            <div class="my-3">
                <button type="submit" class="btn btn-primary" @click="submitLogin">Login</button>
            </div>
        </form>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: ''
        }
    },
    
    methods:{
        submitLogin(){
            //check if the password does not contain a * character
            //check if the email and password exist in the database
            console.log(this.email, this.password)
        }
    }

}
</script>