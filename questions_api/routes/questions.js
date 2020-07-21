const router = require('express').Router();
const Question = require("../models/Questions");
const Subject = require("../models/Subjects");
const { passportJWT , checkAccess} = require("../utils/commonfunctions");



// All CRUD OPERATIONS INLUDED WITH MIDDLEWARES FOR ROLE ACCESS

router.get("/all" ,passportJWT,checkAccess , async (req,res) => {
    let data = await Question.find();
    if(data.length > 0){
        return res.status(200).json(data);
    }
    return res.status(200).json({
        message:`No data found`,
        success:true
    });
});

router.post("/create" ,passportJWT,checkAccess , async (req,res) => {
    // Add middle wares
    await createQuestion(req,res);
});

router.post("/update" ,passportJWT,checkAccess , async (req,res) => {
    // Add middle wares
    await updateQuestion(req,res);
});

router.delete("/delete" ,passportJWT,checkAccess , async (req,res) => {
    // Add middle wares
    await deleteQuestion(req,res);
});

const deleteQuestion = async(req,res) =>{
    try {
        let id = req.body.id.trim();
        
        if(id.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let questionfound = await Question.findById(id);

        if(questionfound){
            await Question.deleteOne({_id:id});        
            return res.status(200).json({
                message:`Question deleted successfully`,
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

const updateQuestion = async(req,res) =>{
    try {
        let id = req.body.id.trim();
        let question = req.body.question.trim();
        let a = req.body.a.trim();
        let b = req.body.b.trim();
        let c = req.body.c.trim();
        let answer = req.body.answer.trim();
        let subject = req.body.subject.trim();
        
        if(id.length == 0 || question.length == 0 || a.length == 0 || b.length == 0 || c.length == 0 || answer.length == 0 || subject.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        let questionfound = await Question.findById(id);
        let valid_id = await Subject.findOne({_id:subject});

        if(questionfound && valid_id){
            let update_details = {
                question : question,
                a : a,
                b : b,
                c : c,
                answer : answer,
                subject : subject
            };
            await Question.updateOne({_id:id},update_details,{runValidators:true});        
            return res.status(200).json({
                message:`Question updated successfully`,
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

const createQuestion = async(req,res) =>{
    try {
        let question = req.body.question.trim();
        let a = req.body.a.trim();
        let b = req.body.b.trim();
        let c = req.body.c.trim();
        let answer = req.body.answer.trim();
        let subject = req.body.subject.trim();

        if(question.length == 0 || a.length == 0 || b.length == 0 || c.length == 0 || answer.length == 0 || subject.length == 0){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }


        let valid_id = await Subject.findOne({_id:subject});
        if(!valid_id){
            return res.status(400).json({
                message:`Invalid details`,
                success:false
            });
        }

        const newQuestion = new Question({
            question : question,
            a : a,
            b : b,
            c : c,
            answer : answer,
            subject : subject
        });

        await newQuestion.save();        
        return res.status(201).json({
            message:`Question created successfully`,
            success:true
        });
      

        
    } catch (error) {
        return res.status(500).json({
            // message: error.message,
            message: `Something went wrong`,
            success: false
          });
    }
};



module.exports = router;