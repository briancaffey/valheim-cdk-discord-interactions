import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk"},
    packages=setuptools.find_packages(where="cdk"),

    install_requires=[
        "aws-cdk.core==1.92.0",
        "aws-cdk.aws_applicationautoscaling==1.92.0",
        "aws-cdk.aws_datasync==1.92.0",
        "aws-cdk.aws_lambda==1.92.0",
        "aws-cdk.aws_s3==1.92.0",
        "aws_cdk.aws_s3_deployment==1.92.0",
        "aws-cdk.aws_apigateway==1.92.0",
        "cdk-valheim==0.0.16",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
