var request = require('supertest')("127.0.0.1:8000");
var expect = require('chai').expect;
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'tobi' });
});


describe("Tests REST API, on the beckend(python->django->drf), and retrive some risk types info", function () {

  it("Site is up", function (done) {
    request
      .get('/')
      .expect(404)
        .end(function(err, res) {
            if (err) return done(err);
            done();
      });
  })
  
  it("REST endpoint is up and returns a JSON file", function (done) {
    request
        .get('/snippets/')        
        .expect(200)
        .expect('Content-Type', /json/)
        .end(function(err, res) {
            if (err) return done(err);
            done();
        })
  })
  
  it("Retrieves a single record from REST API", function (done) {
    request
        .get('/snippets/1')      
        .end(function(err, res) {
            if (!('risk_type_name' in res.body) && !('field_info' in res.body) && !('enum_value' in res.body ) && !('field_name' in res.body) && !('field_type' in res.body )) {
                throw new Error('JSON ill formatted');
            }
            done();
        })
  })

  it("Retrieves all records from REST API.", function (done) {
    request
        .get('/snippets/')      
        .end(function(err, res) {
            if (!(res.body.length>1)) {
                throw new Error('No records returned');
            }
            done();
        })
  })
});

