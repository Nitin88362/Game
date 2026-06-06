const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'one.html'));
});

app.get('/one', (req, res) => {
  res.sendFile(path.join(__dirname, 'one.html'));
});

app.get('/two', (req, res) => {
  res.sendFile(path.join(__dirname, 'two.html'));
});

app.get('/three', (req, res) => {
  res.sendFile(path.join(__dirname, 'three.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
