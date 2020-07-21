const { Schema, model } = require("mongoose");

const UserSchema = new Schema(
  {
    method: {
        type: String,
        enum: ['google', 'github'],
        required: true
    },
    google: {
      id: { type: String },
      displayname: { type: String },
      imageurl: { type: String },
      email: { type: String, lowercase: true }
    },
    github: {
      id: { type: String },
      displayname: { type: String },
      imageurl: { type: String },
      email: { type: String, lowercase: true }
    },
    role :{
      type: String,
      default: "user",
      enum: ["user","admin","superuser"]
    }
  },
  { timestamps: true }
);

module.exports = model("users", UserSchema);