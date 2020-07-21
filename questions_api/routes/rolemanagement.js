const router = require('express').Router();
const RoleManagement = require("../models/RoleManagement");
const { passportJWT , superuser_specific_access_only} = require("../utils/commonfunctions");


router.get("/all" ,passportJWT, superuser_specific_access_only ,async(req,res) => {
    let data = await RoleManagement.find();
    if(data.length > 0){
        return res.status(200).json(data);
    }
    return res.status(200).json({
        message:`No data found`,
        success:true
    });
});

router.post("/addrole",passportJWT, superuser_specific_access_only,async(req,res) => {
   try {
    let url = req.body.url.trim();
    let allowed = req.body.allowed.trim();
    // console.log("allowed",allowed);
    let rolemanagementfound = await RoleManagement.findOne({url : url });

    if(rolemanagementfound){

        if(rolemanagementfound.allowed.includes(allowed)){
            res.status(201).json({
                            message: `Role already exists for the url`,
                            status:true
                        });
        }else{
            rolemanagementfound.allowed.push(allowed);
            rolemanagementfound.save();
            res.status(201).json({
                message: `Role added succesfully`,
                status:true
            });
        }

    }else{
        return res.status(500).json({
            message: `Please verify input details`,
            success: false
        });
    }
   } catch (error) {
        return res.status(500).json({
            // message: error.message,
            message: `Something went wrong`,
            success: false
        });
    }

});

router.post("/addnew",passportJWT, superuser_specific_access_only,async(req,res) => {
    try {
     let url = req.body.url.trim();
     let allowed = req.body.allowed;
    //  console.log("allowed",allowed);
     let rolemanagementfound = await RoleManagement.findOne({url : url });
 
     if(!rolemanagementfound){
         let newRole = new RoleManagement({
             url:url,
             allowed:allowed
         })
         newRole.save();

         res.status(201).json({
             message: `New url and role added succesfully`,
             status:true
         });
     }else{
        return res.status(400).json({
            message:`url already exists`,
            success:false
        });
     }
    } catch (error) {
         return res.status(500).json({
            //  message: error.message,
             message: `Something went wrong`,
             success: false
         });
     }
 
});

router.delete("/deleterole",passportJWT, superuser_specific_access_only,async(req,res) => {
    try {
     let url = req.body.url.trim();
     let denied = req.body.denied.trim();
     let rolemanagementfound = await RoleManagement.findOne({url : url});
 
     if(rolemanagementfound && rolemanagementfound.allowed.includes(denied)){
        
        rolemanagementfound.allowed = rolemanagementfound.allowed.filter(e => e !== denied);
        rolemanagementfound.save();
        res.status(200).json({
                        message: `Role deleted sucessfully for the url`,
                        status:true
                    });
            
 
     }else{
         return res.status(500).json({
             message: `Please verify input details`,
             success: false
         });
     }
    } catch (error) {
         return res.status(500).json({
            //  message: error.message,
             message: `Something went wrong`,
             success: false
         });
     }
 
});

module.exports=router;