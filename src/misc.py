import random

class Misc:
    @staticmethod
    def loaderx():
        n = random.randint(0,2) 
        loader = ["🔄 Loading... Hold on tight!","⏳ AI is brewing your content potion...","🌟 The AI is working its magic...","🤖 Processing your request... AI at work!",]
        return n,loader


    @staticmethod  
    def footer():
        ft = """
        <style>
        a:link , a:visited{
        color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
        background-color: transparent;
        text-decoration: none;
        }

        a:hover,  a:active {
        color: #0283C3; /* theme's primary color*/
        background-color: transparent;
        text-decoration: underline;
        }

        #page-container {
        position: relative;
        min-height: 10vh;
        }

        footer{
            visibility:hidden;
        }

        .footer {
        position: relative;
        left: 0;
        top:-25px;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #808080; /* theme's text color hex code at 50 percent brightness*/
        text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
        }
        </style>

        <div id="page-container">

        <div class="footer">
        <p style='font-size: 0.875em;'><a style='display: inline; text-align: left;'></a><br 'style= top:3px;'>
        By <a style='display: inline; text-align: left;' href="https://github.com/SiddharthSky" target="_blank">SiddharthSky⚡</a></p>
        </div>

        </div>
        """
        return ft
