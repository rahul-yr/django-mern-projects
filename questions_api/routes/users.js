const router = require('express').Router();
const JWT = require('jsonwebtoken');
require('../middlewares/passport');
const { SECRET } = require("../config");
const { passport_google} = require("../utils/commonfunctions");


const signGoogleToken = user => {
    return JWT.sign(
        {
          user_id: user._id,
          // method:user.method,
          displayname: user.google.displayname,
          email: user.google.email,
          type: user.role
        },
        SECRET,
        { expiresIn: "7 days" }
      );
    };


router.get("/auth/google",passport_google,async(req,res) => {
    // console.log("req.body",req.body);
    // console.log("req.user",req.user);
    
    let token = signGoogleToken(req.user)
    let result = {
        token: `Bearer ${token}`,
        expiresIn: 168
      };
    res.status(200).json({
        ...result,
    });
});


// router.get("/res",passportJWT,async(req,res) => {

//     let id = req.user._id;
//     let gid = req.user.google.id;
//     let email = req.user.google.email;
//     let displayname = req.user.google.displayname;
//     let type = req.user.role;
    
//     // console.log(req.originalUrl)

//     res.status(200).json({
//         id,
//         gid,
//         email,
//         displayname,
//         type,
//         message:`Token Verified`,
//         success:true
//     });
// });


module.exports = router;