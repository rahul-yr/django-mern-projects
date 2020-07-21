const { Schema, model } = require("mongoose");
const MongoPaging = require('mongo-cursor-pagination');

const SubjectSchema = new Schema(
  {
    name: { type: String, required: true},
    level: { type: String, required: true},
    domain: { type: String, required: true },
    topic: { type: String, required: true },
    istopicpremium: { type: String, enum: ['yes', 'no'] , default:'no'},
    istopicpublished: { type: String, enum: ['yes', 'no'] , default:'no'},
    issubjectpremium: { type: String, enum: ['yes', 'no'] , default:'no'},
    issubjectpublished: { type: String, enum: ['yes', 'no'] , default:'no'}
  },
  { timestamps: true }
);

SubjectSchema.plugin(MongoPaging.mongoosePlugin);

module.exports = model("subjects", SubjectSchema);