Title: Moving to Amazon S3
Date: 2013-06-23
Tags: news, web
Slug: amazon-s3
Excerpt: A run-through of how to host a static website on S3.

## Moving to Amazon S3 &raquo;

I recently moved my blog to [Amazon S3][s3]. This is a quick outline of the steps involved in setting up a static website on S3.

Why use S3 for hosting a website? Because it is reliable, fast and inexpensive[^amazon]. Moreover, it plays really nicely with [Pelican][pelican2], making it as simple as typing `make s3_upload` into the terminal to regenerate the entire website and push the updated content to your s3 bucket.

I am using [Pelican][pelican2], a static blog engine written in Python to generate my website. Pelican converts [Markdown][md] or [reStructuredText][rst] files into HTML. It supports user-customizable themes (JS/CSS) and templating using [Jinja2][jinja2], a powerful Python template engine, which allows one to customize the final look. 

I will write about why I chose a static blog engine[^pelican] as my backend at another time but for now two words should summarize the most important reasons for me: simplicity and speed. Another reason is its modular structure: Pelican's core functionalities can be extended using plugins. I plan to write plugins for my own purposes for things like **Mendeley**, **Figshare** and **ORCID** [^python]. More on this later.

## Creating S3 buckets &raquo;
Assuming that your domain is **mysite.com**, go into Amazon's [AWS console][awsconsole] and create two buckets: '**mysite.com**' and '**www.mysite.com**'. The bucket with the root domain name will contain the website content while the second bucket will be used to redirect requests from **www.mysite.com** to **mysite.com**.

In properties for **mysite.com**, choose '*Enable website hosting*' under '**Static web hosting**'. Set '**Index document**' to '*index.html*'.

For the **www.mysite.com** bucket, choose '*redirect all requests to another host name*' under '**Static web hosting**'.

## Pushing content to S3 &raquo;

Now comes the fun part: putting content up on the S3 bucket you have just created.

For this, install [s3cmd][s3cmd] via [pip][pip]:

	$ pip install s3cmd

s3cmd is a command line tool for managing data in Amazon S3. For the initial set up, you need to provide your Amazon credentials, i.e. your AWS access key and secret key[^awskey]:

	$ s3cmd --configure

That's almost it. Now any time you want to rebuild your website and push content to S3, just type:

	$ make s3_upload

This uses a little script in the '**Makefile**' file that is provided with your Pelican installation. You only have to enter your S3 bucket name in this file. Once this is done, every time you add or edit content, all you need to do to update your website is run this command again.

## Routing through Amazon's Route 53 &raquo;

Finally, if you are using a custom domain name (**mysite.com** in our example) you have to configure Amazon's [Route 53][R53] as your domain name system (DNS) provider. For details, check out Amazon's documentation on setting up [Route 53][Route53]. You essentially have to set up an alias record for **mysite.com** to map your root domain to the Amazon S3 website endpoint and a CNAME record to map **www.mysite.com** to the corresponding S3 bucket. Finally, replace the current name server record of your current DNS provider with the 4 name servers from Amazon Route 53.

## Bonus: Version Control With Git &raquo;

If you follow the above steps you are all set to host your static html/css/js files on Amazon S3. However, the underlying Markdown/RST and Python files are not backed up this way. You could just upload your entire website content to S3, but there is a more elegant solution, in particular if you are interested in version control à la Subversion: [Git](http://git-scm.com/). Git requires some getting used to but luckily there are several good tutorials around[^git1] [^git2]. 

Once your website is version controlled via Git, it is just a `git push origin master` command away from being backed up on [Github](https://github.com/)[^github]. This not only increases transparency of your work but is also very much in the spirit of open source/open science. The beauty part of such a system is its flexibility: beyond a personal website, a static file engine can also be used to generate anything relating to your research such as manuscripts, reports and electronic lab notebooks[^ELN]. This is something I am seriously considering and working on. Stay tuned.

[R53]: http://aws.amazon.com/route53/
[Route53]: http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html#root-domain-walkthrough-switch-to-route53-as-dnsprovider
[pip]: https://pypi.python.org/pypi/pip
[s3cmd]: http://s3tools.org/s3cmd
[awsconsole]: http://aws.amazon.com/console
[s3]: http://aws.amazon.com/s3
[pelican2]: http://getpelican.com
[rst]: http://docutils.sourceforge.net/rst.html
[md]: http://daringfireball.net/projects/markdown
[jinja2]: http://jinja.pocoo.org/docs
[^pelican]: Check out Duncan Lock's blog for some good arguments for using static website engines: <http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1>
[^python]: with my currently *very* limited Python knowledge. All three services provide APIs that can be utilized to pull in data.
[^amazon]: In fact it is free for the first year if you don't need more than 5GB of storage. Just sign up for AWS Free Usage Tier.
[^awskey]: <http://docs.aws.amazon.com/fws/1.1/GettingStartedGuide/index.html?AWSCredentials.html>
[^git1]: <http://gitready.com>
[^git2]: <http://git-scm.com/book/en/Git-Basics>
[^ELN]: One great example of a fully open, version controlled lab notebook which uses a static file engine is Carl Boettiger's lab notebook: <http://carlboettiger.info/lab-notebook.html>
[^github]: You can find the github repo of this website here: <https://github.com/cbudjan/cbudjan.com>