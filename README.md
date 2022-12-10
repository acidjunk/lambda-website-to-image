# lambda-website-to-image

A simple function that makes a screenshot of a website

Create a lambda function with the 3 needed layers; then you can test it with:

```bash
aws lambda invoke --function-name COPY_PASTED_LAMBDA_ARN log
```

## Scheduler

Now you're ready to add a schedule:
Log in to the AWS console and go to `Cloud watch`, `Events`, `Rules`, `Create rule`.

There you can create a schedule and use it to trigger the lambda function execution.
**Note:** the dropdown will only show/allow functions in th same AWS region.

## Docs and info used:

Selenium lambda tutorial: https://dev.to/awscommunity-asean/creating-an-api-that-runs-selenium-via-aws-lambda-3ck3

Chromedrive lambda layer: https://github.com/diegoparrilla/headless-chrome-aws-lambda-layer

Pillow lambda layer: https://github.com/keithrozario/Klayers#option-2-download-copy-of-layer

Scheduler: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html
