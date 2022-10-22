<template>
    <div class="row">
        <div class="col-md-6 offse-md-3">
            <div>
                <h3>Login</h3>
                <hr />
            </div>
            <form @submit.prevent="submitLogin">
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" class="form-control" placeholder="Enter email" v-model="email">

                </div>
                <div class="error text-danger" v-if="this.errMail">
                    {{ this.errMail }}
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" class="form-control" placeholder="Enter password" v-model="password">

                </div>
                <div class="error text-danger" v-if="this.errPass">
                    {{ this.errPass}}
                </div>
                <div class="my-3">
                    <button type="submit" class="btn btn-primary">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>

import router from '@/router';
import signInValidations from '../services/signInValidations';

export default {
    data() {
        return {
            email: '',
            password: '',
            errMail: '',
            errPass: '',
        }
    },

    methods: {
        submitLogin() {
            let validations = new signInValidations(this.email, this.password);
            this.errMail = validations.checkEmail();
            this.errPass = validations.checkPassword();
            if (this.errMail != '') {
                return this.errMail;
            }
            else if (this.errPass != '') {
                return this.errPass;
            }
            else{
                router.push('./home-page');
            }

        }
    }
}
</script>