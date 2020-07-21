const router = require('express').Router();
const Subject = require("../models/Subjects");
const { passportJWT , checkAccess} = require("../utils/commonfunctions");
// All CRUD OPERATIONS INLUDED WITH MIDDLEWARES FOR ROLE ACCESS

router.get("/all" , passportJWT,checkAccess ,async (req,res) => {
    let data = await Subject.find();
    if(data.length > 0){
        return res.status(200).json(data);
    }
    return res.status(200).json({
        message:`No data found`,
        success:true
    });
});

router.post("/create" , passportJWT,checkAccess, async (req,res) => {
    // Add middle wares
    await createSubject(req,res);
  
});

router.post("/update-subject-status" ,passportJWT,checkAccess, async (req,res) => {
    // Add middle wares
    await updateSubjectStatus(req,res);
});

router.post("/update-topic-status" , passportJWT,checkAccess,async (req,res) => {
    // Add middle wares
    await updateTopicStatus(req,res);
});

router.delete("/delete-subject" ,passportJWT,checkAccess, async (req,res) => {
    // Add middle wares
    await deleteSubject(req,res);
  
});

router.delete("/delete-level" ,passportJWT,checkAccess, async (req,res) => {
    // Add middle wares
    await deleteLevel(req,res);
  
});

router.delete("/delete-topic" , passportJWT,checkAccess, async (req,res) => {
    // Add middle wares
    await deleteTopic(req,res);
  
});

const updateSubjectStatus = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let domain = req.body.domain.trim();
        let issubjectpremium = req.body.issubjectpremium.trim();
        let issubjectpublished = req.body.issubjectpublished.trim();

        
        if(name.length == 0 || domain.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let subjectfound = await Subject.findOne({
            name : name,
            domain : domain
        });

        if(subjectfound){
            let update_details = {issubjectpremium:issubjectpremium,issubjectpublished:issubjectpublished};
            await Subject.updateMany({name : name,domain : domain},update_details ,{runValidators:true});        
            return res.status(200).json({
                message:`Subject Status updated successfully`,
                success:true
            });
        }else{
            return res.status(404).json({
                message:`Please verify input details`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};

const updateTopicStatus = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let level = req.body.level.trim();
        let domain = req.body.domain.trim();
        let topic = req.body.topic.trim();
        let istopicpremium = req.body.istopicpremium.trim();
        let istopicpublished = req.body.istopicpublished.trim();
        
        if(name.length == 0 || domain.length == 0 || level.length == 0 || topic.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let subjectfound = await Subject.findOne({
            name : name,
            level : level,
            domain : domain,
            topic:topic
        });

        if(subjectfound){
            let update_details = {istopicpremium:istopicpremium,istopicpublished:istopicpublished};
            await Subject.updateOne({name : name,level : level, domain : domain , topic:topic},update_details,{runValidators:true});        
            return res.status(200).json({
                message:`Topic Status updated successfully`,
                success:true
            });
        }else{
            return res.status(404).json({
                message:`Please verify input details`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};


const deleteTopic = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let level = req.body.level.trim();
        let domain = req.body.domain.trim();
        let topic = req.body.topic.trim();

        if(name.length == 0 || domain.length == 0 || level.length == 0 || topic.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let subjectfound = await Subject.findOne({
            name : name,
            level : level,
            domain : domain,
            topic:topic
        });

        if(subjectfound){
            await Subject.deleteOne({name : name,level : level, domain : domain , topic:topic});        
            return res.status(200).json({
                message:`Topic deleted successfully`,
                success:true
            });
        }else{
            return res.status(404).json({
                message:`Please verify input details`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};


const deleteLevel = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let level = req.body.level.trim();
        let domain = req.body.domain.trim();

        if(name.length == 0 || domain.length == 0 || level.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let subjectfound = await Subject.findOne({
            name : name,
            level : level,
            domain : domain
        });

        if(subjectfound){
            await Subject.deleteMany({name : name,level : level, domain : domain});        
            return res.status(200).json({
                message:`Level deleted successfully`,
                success:true
            });
        }else{
            return res.status(404).json({
                message:`Please verify input details`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};

const deleteSubject = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let domain = req.body.domain.trim();

        if(name.length == 0 || domain.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let subjectfound = await Subject.findOne({
            name : name,
            domain : domain
        });

        if(subjectfound){
            await Subject.deleteMany({name : name,domain : domain});        
            return res.status(200).json({
                message:`Subject deleted successfully`,
                success:true
            });
        }else{
            return res.status(404).json({
                message:`Please verify input details`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};


const createSubject = async(req,res) =>{
    try {
        let name = req.body.name.trim();
        let level = req.body.level.trim();
        let domain = req.body.domain.trim();
        let topic = req.body.topic.trim();

        if(name.length == 0 || domain.length == 0 || level.length == 0 || topic.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }
        

        let validstatus = await validSubjectFields(name,level,domain,topic);

        if(validstatus){
            const newSubject = new Subject({
                name : name,
                level : level,
                domain : domain,
                topic : topic
            });
    
            await newSubject.save();        
            return res.status(201).json({
                message:`All details are added successfully`,
                success:true
            });
        }else{
            return res.status(400).json({
                message:`Details already exists`,
                success:false
            });
        }

        
    } catch (error) {
        return res.status(500).json({
            message: `Something went wrong`,
            success: false
          });
    }
};


const validSubjectFields = async (name,level,domain,topic) =>{
    let subject = await Subject.findOne({
        name : {$regex : new RegExp(name , "i")},
        level : {$regex : new RegExp(level , "i")},
        domain : {$regex : new RegExp(domain,"i")},
        topic : {$regex : new RegExp(topic,"i")}
    });
    return subject ? false : true;
};

module.exports = router;