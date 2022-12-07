<template>
<div class="my-3 col-md-6 offse-md-3">
        <button type="button" class="btn btn-primary" @click="caregiverPage">Home</button>

        <button style="margin-left:10%" class="btn btn-primary" @click="SignOut">Sign Out</button>

    </div>

    <div class="container py-5 justify-content-center align-items-center">
        <div class="text-center">
            <h1 style="color: #0D6EFD;">Patient Information</h1>
            <hr />
        </div>
        <form @submit.prevent="addPatient">
            <div class="card">
                <MDBAccordion v-model="activeItem" stayOpen>
                    <MDBAccordionItem headerTitle="Patient Information" collapseId="patient">
                        <form class="row container h-100  justify-content-center align-items-center">
                            <div class="row">
                                <div class="col">
                                    <label class="col-form-label">Full Name</label>
                                    <input type="text" class="form-control" placeholder="Full Name" v-model="fullName">
                                </div>
                                <div class="col">
                                    <label class="col-form-label">Gender</label>
                                    <select class="form-control" v-model="gender">
                                        <option value="male">Male</option>
                                        <option value="female">Female</option>
                                        <option value="other">Other</option>
                                    </select>
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Date of Birth</label>
                                    <input type="text" class="form-control" placeholder="Date of Birth (YYYY-MM-DD)"
                                        v-model="dateOfBirth">
                                </div>
                            </div>
                            <div class="row">
                                <div class="form-group col">
                                    <label class="col-form-label">Address</label>
                                    <input type="text" class="form-control"
                                        placeholder="211B Baker Street London, England" v-model="address">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Phone Number</label>
                                    <input type="text" class="form-control" placeholder="506 555 5555">
                                </div>
                            </div>
                            <div class="row">
                                <div class="form-group col">
                                    <label class="col-form-label">Employer</label>
                                    <input type="text" class="form-control" placeholder="UNB" v-model="employer">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Employer Address</label>
                                    <input type="text" class="form-control" placeholder="100 Tucker Park Road"
                                        v-model="employerAddress">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Position</label>
                                    <input type="text" class="form-control" placeholder="Professor" v-model="position">
                                </div>
                            </div>
                        </form>
                    </MDBAccordionItem>

                    <MDBAccordionItem headerTitle="Emergency Contact Information" collapseId="emergency">
                        <form class="row container h-100  justify-content-center align-items-center">
                            <div class="row">
                                <div class="col">
                                    <label class="col-form-label">Full Name</label>
                                    <input type="text" class="form-control" placeholder="Full Name"
                                        v-model="econtactName">
                                </div>
                                <div class="col">
                                    <label class="col-form-label">Relationship</label>
                                    <input type="text" class="form-control" placeholder="Brother/Sister/..."
                                        v-model="econtactRelation">
                                </div>
                            </div>
                            <div class="row">
                                <div class="form-group col">
                                    <label class="col-form-label">Address</label>
                                    <input type="text" class="form-control"
                                        placeholder="211B Baker Street London, England" v-model="econtactAddress">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Phone Number</label>
                                    <input type="text" class="form-control" placeholder="506 555 5555"
                                        v-model="econtactPhoneNumber">
                                </div>

                            </div>
                        </form>
                    </MDBAccordionItem>
                    <MDBAccordionItem headerTitle="Insurance" collapseId="insurance">
                        <form class="row container h-100  justify-content-center align-items-center">
                            <div class="row">
                                <div class="col">
                                    <label class="col-form-label">Insurance Company</label>
                                    <input type="text" class="form-control" placeholder="Insurance Company Name"
                                        v-model="insuranceCompany">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Insured Party</label>
                                    <input type="text" class="form-control" placeholder="Insured Party"
                                        v-model="insuredParty">
                                </div>
                            </div>
                            <div class="row">
                                <div class="col">
                                    <label class="col-form-label">Policy Number</label>
                                    <input type="text" class="form-control" placeholder="86464 687815 89846"
                                        v-model="policyNumber">
                                </div>
                                <div class="col">
                                    <label class="col-form-label">Group Number</label>
                                    <input type="text" class="form-control" placeholder="1738 5494"
                                        v-model="groupNumber">
                                </div>
                                <div class="form-group col">
                                    <label class="col-form-label">Relationship</label>
                                    <input type="text" class="form-control" placeholder="Brother/Sister/..."
                                        v-model="relationship">
                                </div>
                            </div>
                        </form>
                    </MDBAccordionItem>
                </MDBAccordion>
                <div class="text-center mt-2">
                    <button type="submit" class="btn btn-primary btn-lg btn-block" style="width: 100%;">Submit</button>
                </div>
            </div>

        </form>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';
import { MDBAccordion, MDBAccordionItem } from "mdb-vue-ui-kit";
import { ref } from "vue";

export default {
    components: {
        MDBAccordion,
        MDBAccordionItem
    },

    data() {
        return {
            users: [],
            activeItem: ref('patient'),
            fullName: '',
            gender: '',
            address: '',
            patientImage: '',
            phoneNumber: '',
            employer: '',
            employerAddress: '',
            position: '',
            dateOfBirth: '',
            caregiverEmail: localStorage.getItem('email'),
            caregiverName: localStorage.getItem('name'),
            econtactName: '',
            econtactRelation: '',
            econtactAddress: '',
            econtactPhoneNumber: '',
            insuranceCompany: '',
            insuredParty: '',
            policyNumber: '',
            groupNumber: '',
            relationship: '',
        }
    },
    methods: {

        async addPatient() {
            const patientProfile = {
                method: 'post',
                url: 'http://localhost:5000/',
                fullName: this.fullName,
                gender: this.gender,
                address: this.address,
                patientImage: this.patientImage,
                phoneNumber: this.phoneNumber,
                employer: this.employer,
                employerAddress: this.employerAddress,
                position: this.position,
                dateOfBirth: this.dateOfBirth,
                caregiverEmail: this.caregiverEmail,
                caregiverName: this.caregiverName,
                econtactName: this.econtactName,
                econtactRelation: this.econtactRelation,
                econtactAddress: this.econtactAddress,
                econtactPhoneNumber: this.econtactPhoneNumber,
                insuranceCompany: this.insuranceCompany,
                insuredParty: this.insuredParty,
                policyNumber: this.policyNumber,
                groupNumber: this.groupNumber,
                relationship: this.relationship,
                purpose: 'profileUpdate',
                headers: {
                    'Content-Type': 'application/json, multipart/form-data'
                }
            }

            await axios.post('http://localhost:5000/addPatient', patientProfile).then((res) => {
                if (res.data.status === 'success') {
                    console.log(res.data.status);
                    console.log(res);
                    //get the role and detemine the page to direct the user to
                    const role = localStorage.getItem('role');
                    if (role === 'admin') {
                        router.push('/admin-home-page');
                    } else if (role === 'caregiver') {
                        router.push('/caregiver-home-page');
                    } else if (role === 'manager') {
                        router.push('/manager-home-page');
                    }
                } else {
                    console.log(res.data.status);
                }
            }).catch((err) => {
                console.log(err);
            })


        },

        SignOut() {
            localStorage.clear();
            router.push('./login-page');
        },
        
        caregiverPage() {
            router.push('/caregiver-home-page');
        },

    },
}

</script>