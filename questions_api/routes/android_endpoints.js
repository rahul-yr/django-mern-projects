const router = require('express').Router();
const Question = require("../models/Questions");
const Subject = require("../models/Subjects");
const { passportJWT , checkAccess} = require("../utils/commonfunctions");



// All CRUD OPERATIONS INLUDED WITH MIDDLEWARES FOR ROLE ACCESS

router.get("/subjects", async(req,res) => {
    try {
        let opts = {name:"Python"};
        
        let limitcount = 3;
        if(req.body.next){
            let data = await Subject.paginate({limit : limitcount,query:opts ,next:req.body.next});
            return res.status(200).json({data});
        }else if(req.body.previous){
            let data = await Subject.paginate({limit : limitcount,query:opts ,previous:req.body.previous });
            return res.status(200).json({data});
        }else{
            let data = await Subject.paginate({limit : limitcount,query:opts });
            return res.status(200).json({data});
        }
    } catch (error) {
        return res.status(404).json({
            message:error.message,
            success:false
        });

    }
});

module.exports = router;