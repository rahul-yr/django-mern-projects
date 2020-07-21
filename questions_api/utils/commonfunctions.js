const passport = require('passport');
const RoleManagement = require("../models/RoleManagement");

const superuser_specific_access_only = (req, res, next) =>{
    (req.user.role == "superuser") ? next() : res.status(401).json("Privilege access required");
}

const passport_google = passport.authenticate("googleToken",{session:false});

const passportJWT = passport.authenticate('jwt', { session: false });


const checkAccess = async(req,res,next) =>{
    let data = await RoleManagement.findOne({url:req.originalUrl});
    if(data && data.allowed.includes(req.user.role)){
        next();
    }else{
        res.status(401).json("Access denied");
    }
}

module.exports = {
    superuser_specific_access_only,
    passport_google,
    passportJWT,
    checkAccess
}

