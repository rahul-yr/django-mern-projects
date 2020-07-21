const { Schema, model } = require("mongoose");

const RoleManagementSchema = new Schema(
  {
    url: { type: String, required: true},
    allowed: [{ type: String}]
  },
  { timestamps: true }
);

module.exports = model("rolemanagements", RoleManagementSchema);