var express = require('express');
var bodyParser = require('body-parser');

//ML Aspects with Brainjs
const brain = require('brain.js');
const data = require('./data.json');

const network = new brain.recurrent.LSTM();

const trainingData = data.map(item => ({
  input: item.text,
  output: item.category
}));

network.train(trainingData, {
  iterations: 2000
});


// Express App Initialized
var app = express();
var urlencodedParser = bodyParser.urlencoded({ extended: false })
app.set('view engine','ejs');


app.get('/',function(req,res){
	// res.send('Hello world this is Express');
	res.render('index');
});


app.get('/predict',function(req,res){
	console.log(req.query);
res.render('index');
})

// Using Body Parser to Parse our data
app.post('/predict',urlencodedParser,function(req,res){
	console.log(req.body);
	const output = network.run(req.body.message);
	console.log(`Category: ${output}`);

res.render('results',{mydata:req.body.message,resultdata:output});
})



app.listen(4000,function(){
	console.log("Listening on localhost:4000");
});