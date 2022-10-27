const express = require('express');
const app = express();
app.listen(1738, () => console.log('Server running on port 1738'));
app.use(express.static('public'));