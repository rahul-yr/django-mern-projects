var passport = require('passport');
const GooglePlusTokenStrategy = require('passport-google-plus-token');
const { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,SECRET } = require("../config");
const User = require("../models/Users");
const JwtStrategy = require('passport-jwt').Strategy;
const { ExtractJwt } = require('passport-jwt');


// Google OAuth Strategy
const google_opts = {
    clientID: GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET
};

passport.use('googleToken', new GooglePlusTokenStrategy(google_opts, 
    async (accessToken, refreshToken, profile, done) => {
    try {
        // Should have full user profile over here
        // console.log('profile', profile);
        // console.log('accessToken', accessToken);
        // console.log('refreshToken', refreshToken);

        const existingUser = await User.findOne({ "google.id": profile.id , "google.email": profile.emails[0].value});
        if (existingUser) {
            // console.log('Existing User');
            return done(null, existingUser);
        }
        const newUser = new User({
            method: 'google',
            google: {
                id: profile.id,
                displayname: profile.displayName,
                imageurl: profile.photos[0].value,
                email: profile.emails[0].value
            }
        });
        
        await newUser.save();
        // console.log("New User");
        done(null, newUser);
    } catch(error) {
        done(error, false, error.message);
    }
}));

// JSON WEB TOKENS STRATEGY
passport.use(new JwtStrategy({
    jwtFromRequest: ExtractJwt.fromHeader('authorization'),
    secretOrKey: SECRET
  }, async (payload, done) => {
    try {
      // Find the user specified in token
      const user = await User.findById(payload.user_id);
  
      // If user doesn't exists, handle it
      if (!user) {
        return done(null, false);
      }
  
      // Otherwise, return the user
      done(null, user);
    } catch(error) {
      done(error, false);
    }
  }));