<template>
    <div class="row container py-5 h-100 d-flex justify-content-center align-items-center">
        <form enctype="multipart/form-data" class="section form-group mt-5 shadow col-md-5 ">
            <div class="row container">
                <div class="col-form-label col-form-label-lg">
                    <label for="Upload Excel">Upload File</label>
                    <input class="small" type='file' accept=".xls" @change="onFileSelected" />
                </div>
            </div>
            <div class="field">
                <button class="btn btn-primary col-3" @click="submitFile">Upload</button>
            </div>
        </form>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    methods: {
        onFileSelected(event) {
            this.selectedFile = event.target.files[0];
        },

        async submitFile() {
            const formData = new FormData();
            formData.append('file', this.selectedFile);
            formData.append('headers', {
                'Content-Type': 'multipart/form-data',
            });

            formData.append('newFileName', localStorage.getItem('email'));
            try {
                await axios.post('http://localhost:5000/excelUpload', formData);
            } catch (error) {
                console.log(error);
            }
        },
    },
};
</script>