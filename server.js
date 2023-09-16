const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Serve your static files (HTML, CSS, JS) from a 'public' directory
app.use(express.static('public'));

// Endpoint to handle faculty chat
app.post('/facultychat', (req, res) => {
  // Log the request body to see what data was sent from the frontend
  console.log('Request body:', req.body);

  // Process the data and send a response if needed
  // Here, you can retrieve the selected professor names and subjects from req.body

  // Send a response (for testing purposes)
  res.json({ message: 'Faculty chat request received!' });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
