<template>
    <div class="row col-md-8 form-group shadow align-items-center">
        <div>
            <h3>Profile</h3>
            <hr />
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Full Name</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter full name" v-model="fullName" />
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Address</label>
            <input type="text" class="form-control form-control-lg" placeholder="Enter address" v-model="address" />
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">What is your gender?</label>
            <select class="form-control" v-model="gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
            </select>
        </div>
        <div class="col-12 form-group">
            <label class="col-form-label col-form-label-lg">Do you have a driver's license?</label>
            <input class="form-check-input mt-3" type="checkbox" v-model="license">
        </div>


        <div class="col-12 form-group text-center">
            <button class="btn btn-primary btn-md col-4" @click="submitProfile">Submit</button>
        </div>
    </div>
</template>

<script>
// import router from '@/router';
export default {
    methods: {
        submitProfile() {
            // router.push('./home-page');
        }
    },
    data: function () {
        return {
            fullName: '',
            address: '',
            license: '',
            gender: '',
        }
    }
}
</script>