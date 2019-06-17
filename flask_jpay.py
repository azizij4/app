#!/usr/bin/python3
from flask import Flask
app = Flask("Jpay")

@app.route('/')
def index():
     return("""<!DOCTYPE html>
<html lang="En">
<head>
	<title>JPAY</title>
	
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap-theme.min.css">
     <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="container-fluid">
		<div class="row">
			
<!-- header-->
	<header>
		<div class="containerCentered">
	
		
      <div class="containercentered bg-success">
        <div class="row">
          <div col-xs-12>
            <table class="table table-stripped" style="width: 99%;">
              <tr>
                <td>
                  
      <a href="contact.html" class="btn btn-xs" data-pa-click="header" pa-marked="1">
        <h1 style="color: gold; font-family: sans-serif; font-size: 50px;">J<small style="color: orange; font-size: 50px;">P<sup>A</sup><b>L</b></small></h1><br>

      </a>
                </td>
                <td align="right">
                <a class="btn btn-sm btn-primary" id="ul-btn" href="#" data-pa-click="Sign Up" pa-marked="1" data-toggle="collapse" data-target="signin">Sign Up</a>
                  <div class="collapse" id="content" >

            
            <div class="well">


            </div>
          </div>
       &nbsp;&nbsp;
      <a class="btn btn-sm btn-default" id="ul-btn" href="#" data-pa-click="login" pa-marked="1">Log In</a>
                </td>
              </tr>
            </table>
          </div>
        </div>
      </div>
  </div>
  </header>
    <!-- end header-->


<!-- start section -->
	<section>
    <div class="container">
      <div class="row">
<div class="sidebar">
  
    <div class="col-xs-3 col-md-4 col-lg-4">
      <ul>
        <li><a href="#" class="active">about</a></li>
        <li><a href="#">team</a></li>
        <li><a href="#">contact</a></li>
      </ul>
    </div>

  
</div>		
<!--end of side bar   -->

<div class="content">
<div class="col-md-8 col-lg- col-xs-8" >
  



</div>
 </div>




<!-- closing  div tags content-->
</div>
</div>



















    
    
	

	</section>

<footer>
	
<div class="sub-footer" >
            <div class="footerInside">
                <div id="footer">
                    <table  class="table  table-condensed">
                        <tbody><tr class="active">
                            <td>
                            	&nbsp;&nbsp;
                                <a class="nav-bottom" href="#" style="color: black">Privacy Policy</a>
                                &nbsp; | &nbsp;
                                <a class="nav-bottom" href="#" style="color: black">Terms and conditions</a>&nbsp;&nbsp;|&nbsp;&nbsp;
                                </td>
                                <td style="text-align: right;">
                                	 <a class="nav-bottom"  href="#" style="color: black; text-align:right;">English</a>
                                 &nbsp; | &nbsp;
                                <a class=""  href="#" style="color: black; text-align:right;">Kiswahili</a> 

                                </td>        
                            </tr>

                    </tbody>
                    <tfoot align="center"><tr>
                    	<div class="container">
                    		<div class="row">
                    			<div class="col-md-4">
                    				
                    			</div>

                    			<div class="col-md-4">
                    			</div>

                    			<div class="col-md-4">
                    				<td align="right"><font color="yellow" size="3">| </font>
                    				<a class=""  href="#" style="color: black; text-align:right;">Feedback</a> </td>
                    			</div>
                    		</div>
                    		
                    	</div>
                    	
                    	
                    </tr> </tfoot></table>
                </div>
            </div>
        </div>
</footer>

	

		</div>

	</div>
	


	<script  src="js/jquery.min.js"></script>
	<script  src="js/bootstrap.min.js"></script>
</body>
</html>

""")
	
@app.route("/menu")
def menu():
     return ""	 
if __name__=="__main__":
    app.run(debug = True)
