const { Schema, model } = require("mongoose");

const QuestionSchema = new Schema(
  {
    question: {
      type: String,
      required: true
    },
    a: {
      type: String,
      required: true
    },
    b: {
        type: String,
        required: true
    },
    c: {
        type: String,
        required: true
    },
    answer: {
        type: String,
        required: true
    },
    subject : [
        {
          type: Schema.Types.ObjectId, ref: 'subjects',
        }
    ]
  },
  { timestamps: true }
);

module.exports = model("questions", QuestionSchema);