const { ObjectId } = require('mongodb')
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const geckoSchema = new Schema({
    geckoName: { type: String, required: true },
    speciesName: { type: String, required: true },
    hatchDate: { type: String, required: true },
    imageUrl: { type: String, required: false},
    gender: { type: String, required: true },
    purchasePrice: { type: Number, required: true },
}, {
    timestamps: true,
});

const Gecko = mongoose.model('Gecko', geckoSchema);

module.exports = Gecko;