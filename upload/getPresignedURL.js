const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const s3 = new AWS.S3()


const URL_EXPIRATION_SECONDS = 300


exports.handler = async (event) => {
  return await getUploadURL(event)
}

const getUploadURL = async function(event) {

  const fileName = 'test.pdf';

  
  const s3Params = {
    Bucket: process.env.UploadBucket,
    Key: fileName, 
    Expires: URL_EXPIRATION_SECONDS,
    ContentType: 'application/pdf',

  }

  console.log('Params: ', s3Params)
  const uploadURL = await s3.getSignedUrlPromise('putObject', s3Params)

  return JSON.stringify({
    uploadURL: uploadURL,
    Key: fileName 
  })
}
