<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x12. JavaScript - Warm up</h1>


  <ul class="list-group metadata" id="project-metadata">
  <li class="list-group-item">
    <i class="fa fa-folder-open fa-fw"></i>
    <em>Foundations &gt; Higher-level programming &gt; JavaScript</em>
  </li>


    <li class="list-group-item">
      <i class="fa fa-user fa-fw"></i> By Guillaume, CTO at Holberton School
    </li>




      <li class="list-group-item">
        <i class="fa fa-calendar fa-fw"></i>
            Ongoing project - started 08-02-2021, must end by 08-03-2021 (in about 15 hours)
          - you're done with <span id="student_task_done_percentage">0</span>% of tasks.
      </li>

      <li class="list-group-item">
        <i class="fa fa-check fa-fw"></i>
          Checker will be released at 08-02-2021 12:00 PM
      </li>


      <li class="list-group-item">
        <i class="fa fa-check-square fa-fw"></i>
        QA review fully automated.
      </li>


</ul>



    <div id="project_id" style="display: none" data-project-id="303"></div>




      

      <div class="gap" id="project-description">
  <h2>Background Context</h2>

<p>JavaScript is used for many things. At Holberton School, you will use JavaScript for 2 reasons:</p>

<ul>
<li>Scripting (same as we did with Python)</li>
<li>Web front-end</li>
</ul>

<p>For the moment, and for learning all basic concepts of this language, we will do some scripting.
After, we will make our AirBnB project dynamic by using Javascript and JQuery.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Writing JavaScript Code" target="_blank">Writing JavaScript Code</a> </li>
<li><a href="/rltoken/iE6zaLw7pybp648IfRmk5Q" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/4td1BbZAYn4Dldi6k0CY7A" title="Data Types" target="_blank">Data Types</a> </li>
<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Operators" target="_blank">Operators</a> </li>
<li><a href="/rltoken/ALCoiVRvxmsjdqCUdWC_lg" title="Operator Precedence" target="_blank">Operator Precedence</a> </li>
<li><a href="/rltoken/Nlfhdy6Thyu_WgtBSqoAUw" title="Controlling Program Flow" target="_blank">Controlling Program Flow</a> </li>
<li><a href="/rltoken/Ta66PZ6_16K3q99oELvjkQ" title="Functions" target="_blank">Functions</a> </li>
<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Objects and Arrays" target="_blank">Objects and Arrays</a> </li>
<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Intrinsic Objects" target="_blank">Intrinsic Objects</a> </li>
<li><a href="/rltoken/mduSK-WOoRe6WohU1p2zZQ" title="Module patterns" target="_blank">Module patterns</a> </li>
<li><a href="/rltoken/kNWuHjyUvjr74wU2hBqd_A" title="var, let and const" target="_blank">var, let and const</a> </li>
<li><a href="/rltoken/qkp1hdLiI8DJje88bxcL6w" title="JavaScript Tutorial" target="_blank">JavaScript Tutorial</a> </li>
<li><a href="/rltoken/ieSajamJQ-Nv3XzcS_d5lA" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/0TM5wHPW2wLPMP_l8lkdOg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to run a JavaScript script</li>
<li>How to create variables and constants</li>
<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
<li>What are all the data types available in JavaScript</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use <code>while</code> and <code>for</code> loops</li>
<li>How to use <code>break</code> and <code>continue</code> statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any <code>return</code> statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant (version 14.x.x). <a href="/rltoken/EK3q1S4Ouo08kTMI42cSig" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/FuXjfOYe18hUXCDoyMxBSg" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/iIDdBVB4HNhPpb_5e5L-Qg" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 10</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="/rltoken/FuXjfOYe18hUXCDoyMxBSg" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

</div>


      

        <h2 class="gap" id="project-quiz-questions-title">
    Quiz questions
  </h2>

  <div class="panel panel-default">
    <div class="panel-body">
        <p id="quiz_questions_collapse_toggle">Show</p>

      <section class="quiz_questions_show_container" style="display: none;">
          <div class="quiz_question_item_container" data-role="quiz_question386" data-position="1">
            <div class=" clearfix" id="quiz_question-386">

    <h4 class="quiz_question">Question #0</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Does Javascript have <code>String</code> as a native datatype?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="386">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797377565" id="quiz-answer-1505797377565" data-quiz-question-id="386" data-quiz-answer-id="1505797377565" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797377565">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797383607" id="quiz-answer-1505797383607" data-quiz-question-id="386" data-quiz-answer-id="1505797383607" disabled="disabled">
  <label for="quiz-answer-1505797383607">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question387" data-position="2">
            <div class=" clearfix" id="quiz_question-387">

    <h4 class="quiz_question">Question #1</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Does Javascript have <code>Array</code> as a native datatype?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="387">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797388926" id="quiz-answer-1505797388926" data-quiz-question-id="387" data-quiz-answer-id="1505797388926" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797388926">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797390881" id="quiz-answer-1505797390881" data-quiz-question-id="387" data-quiz-answer-id="1505797390881" disabled="disabled">
  <label for="quiz-answer-1505797390881">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question388" data-position="3">
            <div class=" clearfix" id="quiz_question-388">

    <h4 class="quiz_question">Question #2</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Does Javascript have <code>Set</code> as a native datatype?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="388">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797395344" id="quiz-answer-1505797395344" data-quiz-question-id="388" data-quiz-answer-id="1505797395344" disabled="disabled">
  <label for="quiz-answer-1505797395344">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797397935" id="quiz-answer-1505797397935" data-quiz-question-id="388" data-quiz-answer-id="1505797397935" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797397935">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question389" data-position="4">
            <div class=" clearfix" id="quiz_question-389">

    <h4 class="quiz_question">Question #3</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>Does Javascript have <code>Dictionary</code> as a native datatype?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="389">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797413125" id="quiz-answer-1505797413125" data-quiz-question-id="389" data-quiz-answer-id="1505797413125" disabled="disabled">
  <label for="quiz-answer-1505797413125">
    <p>Yes</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797417981" id="quiz-answer-1505797417981" data-quiz-question-id="389" data-quiz-answer-id="1505797417981" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797417981">
    <p>No</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->
        <div class="alert alert-info">
            <h4>Tips:</h4>
            <p>Everything is <code>Object</code> and <code>Object</code> type in Javascript is powerful.</p>

        </div>

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question390" data-position="5">
            <div class=" clearfix" id="quiz_question-390">

    <h4 class="quiz_question">Question #4</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What does <code>let</code> mean? (please check all true answers)</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="390">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797439213" id="quiz-answer-1505797439213" data-quiz-question-id="390" data-quiz-answer-id="1505797439213" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797439213">
    <p>It’s the keyword to define a variable in the local scope</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797444995" id="quiz-answer-1505797444995" data-quiz-question-id="390" data-quiz-answer-id="1505797444995" disabled="disabled">
  <label for="quiz-answer-1505797444995">
    <p>It’s the keyword to define a global variable</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797450622" id="quiz-answer-1505797450622" data-quiz-question-id="390" data-quiz-answer-id="1505797450622" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797450622">
    <p>It’s the keyword to define a variable with optionally initializing it to a value</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797459495" id="quiz-answer-1505797459495" data-quiz-question-id="390" data-quiz-answer-id="1505797459495" disabled="disabled">
  <label for="quiz-answer-1505797459495">
    <p>It’s the keyword to define a constant variable</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797464959" id="quiz-answer-1505797464959" data-quiz-question-id="390" data-quiz-answer-id="1505797464959" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797464959">
    <p>It’s the keyword to define a variable that can be re-assign during the execution</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question391" data-position="6">
            <div class=" clearfix" id="quiz_question-391">

    <h4 class="quiz_question">Question #5</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What does <code>const</code> mean? (please check all true answers)</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="391">
                <li class="">
  <input type="checkbox" name="quiz-answer-1505797474591" id="quiz-answer-1505797474591" data-quiz-question-id="391" data-quiz-answer-id="1505797474591" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797474591">
    <p>It’s the keyword to define a variable in the local scope</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797481607" id="quiz-answer-1505797481607" data-quiz-question-id="391" data-quiz-answer-id="1505797481607" disabled="disabled">
  <label for="quiz-answer-1505797481607">
    <p>It’s the keyword to define a global variable</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797486959" id="quiz-answer-1505797486959" data-quiz-question-id="391" data-quiz-answer-id="1505797486959" disabled="disabled">
  <label for="quiz-answer-1505797486959">
    <p>It’s the keyword to define a variable with optionally initializing it to a value</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797491774" id="quiz-answer-1505797491774" data-quiz-question-id="391" data-quiz-answer-id="1505797491774" disabled="disabled" checked="checked">
  <label for="quiz-answer-1505797491774">
    <p>It’s the keyword to define a constant variable</p>

</label></li>

                <li class="">
  <input type="checkbox" name="quiz-answer-1505797497014" id="quiz-answer-1505797497014" data-quiz-question-id="391" data-quiz-answer-id="1505797497014" disabled="disabled">
  <label for="quiz-answer-1505797497014">
    <p>It’s the keyword to define a variable that can be re-assign during the execution</p>

</label></li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>


        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1757" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1757">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. First constant, first print
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints “JavaScript is amazing”:</p>

<ul>
<li>You must create a constant variable called <code>myVar</code> with the value “JavaScript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>0-javascript_is_amazing.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1757">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1757" data-project-id="303" data-toggle="modal" data-target="#task-1757-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1757-users-done-modal" data-task-id="1757" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. First constant, first print"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1757" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1757-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1757-modal" data-task-id="1757" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1757_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1757" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1757" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1758" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1758">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. 3 languages
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints 3 lines:</p>

<ul>
<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “JavaScript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>1-multi_languages.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1758">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1758" data-project-id="303" data-toggle="modal" data-target="#task-1758-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1758-users-done-modal" data-task-id="1758" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. 3 languages"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1758" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1758-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1758-modal" data-task-id="1758" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1758_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1758" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1758" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1759" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1759">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Arguments
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints a message depending of the number of arguments passed:</p>

<ul>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>If only one argument is passed to the script, print “Argument found”</li>
<li>Otherwise, print “Arguments found”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p>Reference: <a href="/rltoken/E5x0rMmgii1g_Da9R7DUag" title="process.argv" target="_blank">process.argv</a></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>2-arguments.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1759">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1759" data-project-id="303" data-toggle="modal" data-target="#task-1759-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1759-users-done-modal" data-task-id="1759" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. Arguments"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1759" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1759-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1759-modal" data-task-id="1759" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1759_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1759" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1759" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1760" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1760">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Value of my argument
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints the first argument passed to it:</p>

<ul>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>length</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>3-value_argument.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1760">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1760" data-project-id="303" data-toggle="modal" data-target="#task-1760-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1760-users-done-modal" data-task-id="1760" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "3. Value of my argument"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1760" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1760-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1760-modal" data-task-id="1760" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1760_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1760" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1760" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1761" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-1761">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Create a sentence
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints two arguments passed to it, in the following format: “<first argument=""> is <second argument="">”</second></first></p>

<ul>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>4-concat.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1761">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1761" data-project-id="303" data-toggle="modal" data-target="#task-1761-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1761-users-done-modal" data-task-id="1761" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "4. Create a sentence"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1761" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1761-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1761-modal" data-task-id="1761" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1761_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1761" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1761" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1762" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-1762">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. An Integer
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>

<ul>
<li>If the argument can’t be converted to an integer, print “Not a number”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>try/catch</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>5-to_integer.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1762">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1762" data-project-id="303" data-toggle="modal" data-target="#task-1762-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1762-users-done-modal" data-task-id="1762" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "5. An Integer"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1762" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1762-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1762-modal" data-task-id="1762" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1762_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1762" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1762" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1763" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-1763">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. Loop to languages
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>

<ul>
<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “JavaScript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use any <code>if/else</code> statement</li>
<li>You can use only one <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>6-multi_languages_loop.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1763">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1763" data-project-id="303" data-toggle="modal" data-target="#task-1763-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1763-users-done-modal" data-task-id="1763" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "6. Loop to languages"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1763" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1763-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1763-modal" data-task-id="1763" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1763_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1763" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1763" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1764" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-1764">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. I love C
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints <code>x</code> times “C is fun”</p>

<ul>
<li>Where <code>x</code> is the first argument of the script</li>
<li>If the first argument can’t be converted to an integer, print “Missing number of occurrences”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You can use only two <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>7-multi_c.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1764">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1764" data-project-id="303" data-toggle="modal" data-target="#task-1764-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1764-users-done-modal" data-task-id="1764" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "7. I love C"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1764" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1764-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1764-modal" data-task-id="1764" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1764_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1764" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1764" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1765" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-1765">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Square
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints a square</p>

<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can’t be converted to an integer, print “Missing size”</li>
<li>You must use the character <code>X</code> to print the square</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>8-square.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1765">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1765" data-project-id="303" data-toggle="modal" data-target="#task-1765-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1765-users-done-modal" data-task-id="1765" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "8. Square"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1765" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1765-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1765-modal" data-task-id="1765" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1765_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1765" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1765" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1766" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-1766">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Add
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that prints the addition of 2 integers</p>

<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: <code>function add(a, b)</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>9-add.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1766">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1766" data-project-id="303" data-toggle="modal" data-target="#task-1766-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1766-users-done-modal" data-task-id="1766" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "9. Add"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1766" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1766-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1766-modal" data-task-id="1766" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1766_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1766" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1766" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1767" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-1767">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. Factorial
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that computes and prints a factorial</p>

<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of <code>NaN</code> is <code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>10-factorial.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1767">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1767" data-project-id="303" data-toggle="modal" data-target="#task-1767-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1767-users-done-modal" data-task-id="1767" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "10. Factorial"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1767" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1767-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1767-modal" data-task-id="1767" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1767_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1767" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1767" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1768" data-position="12" id="task-num-11">
      <div class="panel panel-default task-card " id="task-1768">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Second biggest!
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a script that searches the second biggest integer in the list of arguments.</p>

<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print <code>0</code></li>
<li>If the number of arguments is 1, print <code>0</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>11-second_biggest.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1768">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1768" data-project-id="303" data-toggle="modal" data-target="#task-1768-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1768-users-done-modal" data-task-id="1768" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "11. Second biggest!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1769" data-position="13" id="task-num-12">
      <div class="panel panel-default task-card " id="task-1769">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Object
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>

<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>12-object.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1769">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1769" data-project-id="303" data-toggle="modal" data-target="#task-1769-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1769-users-done-modal" data-task-id="1769" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "12. Object"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>




      <button class="btn btn-default task_containers_modal" data-task-id="1769" data-container-spec-ids="[22]" data-toggle="modal" data-target="#task-containers-1769-modal">
        <i class="fa fa-terminal"></i>&nbsp;
        Get a sandbox
      </button>
      <div class="modal fade task_containers_modal" id="task-containers-1769-modal" data-task-id="1769" data-container-spec-ids="[22]">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">
              <i class="fa fa-terminal"></i>&nbsp;
              Sandboxes
            </h4>
        </div>
        <div class="modal-body">
        <p>Each sandbox will be available for 8 months max</p>

        <div class="panel panel-default" id="task_1769_container_spec_22">

            <!-- Default panel contents -->
            <div class="panel-heading">
                <div class="row">
                    <div class="panel-title col-md-8 text-left">
                        <b>Ubuntu 14.04 - NodeJS 10</b>
                        <span class="container_id"></span>
                    </div>
                    <div class="col-md-4 text-right row">
                        <span class="container_webterm" style="margin-right: 20px;" title="Web terminal (Beta)"></span>
                        <span>
                            <input type="submit" name="commit" value="Start" class="btn btn-primary start_container" data-task-id="1769" data-container-spec-id="22">
                            <input type="submit" name="commit" value="Destroy" class="btn btn-primary destroy_container" data-task-id="1769" data-container-spec-id="22">
                            <div class="spinner">
                                <div class="bounce1"></div>
                                <div class="bounce2"></div>
                                <div class="bounce3"></div>
                            </div>
                        </span>
                    </div>
                </div>
            </div>

            <div class="container_body">
                <div class="panel-body">
                    <div class="container_error alert alert-danger" role="alert"></div>
                    <div class="container_error_limit alert alert-danger" role="alert">
                      <div>
                        <p>
                          You have reached the limit of sandboxes you can spawn
                          (5)<br>
                          Please terminate a running sandbox before starting a new one
                        </p>
                      </div>
                      <div>
                        <a class="btn btn-default" href="/dashboards/my_containers">My sandboxes</a>
                      </div>
                    </div>
                    <table class="table container_info">
                        <thead>
                            <tr>
                                <th class="container_public_access_header">Access from anywhere</th>
                                <th class="container_private_access_header">Access from campus</th>
                                <th>Detailed port mapping</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="container_public_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                        <li class="container_sftp_access">
                                            <span class="fa-li"><i class="fa fa-exchange"></i></span>
                                            <b>SFTP:</b>
                                            <code class="container_sftp"></code>
                                        </li>
                                        <li class="container_scp_access">
                                            <span class="fa-li"><i class="fa fa-files-o"></i></span>
                                            <b>SCP:</b>
                                            <code class="container_scp"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_private_access">
                                    <ul class="fa-ul" style="line-height: 2.0;">
                                        <li class="container_http_access" style="line-height: 1.6;">
                                            <span class="fa-li"><i class="fa fa-globe"></i></span>
                                            <b>HTTP:</b>
                                            <div class="container_http"></div>
                                        </li>
                                        <li class="container_https_access">
                                            <span class="fa-li"><i class="fa fa-lock"></i></span>
                                            <b>HTTPS:</b>
                                            <span class="container_https"></span>
                                        </li>

                                        <li class="container_user_info" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-user"></i></span>
                                            <b>User:</b>
                                            <code class="container_user"></code>
                                        </li>
                                        <li class="container_password_info">
                                            <span class="fa-li"><i class="fa fa-key"></i></span>
                                            <b>Password:</b>
                                            <code class="container_password"></code>
                                        </li>

                                        <li class="container_ssh_access" style="margin-top: 12px;">
                                            <span class="fa-li"><i class="fa fa-terminal"></i></span>
                                            <b>SSH:</b>
                                            <code class="container_ssh"></code>
                                        </li>
                                    </ul>
                                </td>
                                <td class="container_ports"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="error"></div>

        <p class="gap alert alert-info">
            <strong>Ports mapping</strong><br>
            Each exposed port is mapped to another one.
            Example: the port SSH <strong>22</strong> is mapped to the port <strong>33511</strong>.
        </p>
        </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>


</div>

    </div>


</div>

    </div>
    <div data-role="task1770" data-position="14" id="task-num-13">
      <div class="panel panel-default task-card " id="task-1770">
  <span id="user_id" data-id="2639"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      13. Add file
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2639"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a function that returns the addition of 2 integers.</p>

<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be <code>add</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p><a href="/rltoken/M3uMoMlngAtefSYF1c7PNQ" title="Tip" target="_blank">Tip</a> </p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>0x12-javascript-warm_up</code></li>
            <li>File: <code>13-add.js</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->

    <div class="panel-footer">
      
<div>
    <button class="student_task_done btn btn-default no" data-task-id="1770">
      <span class="no"><i class="fa fa-square-o"></i></span>
      <span class="yes"><i class="fa fa-check-square-o"></i></span>
      <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

    <button class="users_done_for_task btn btn-default btn-default" data-task-id="1770" data-project-id="303" data-toggle="modal" data-target="#task-1770-users-done-modal">
      Help
    </button>
    <div class="modal fade users-done-modal" id="task-1770-users-done-modal" data-task-id="1770" data-project-id="303">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "13. Add file"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>

    </div>


</div>

    </div>

    <p class="lg-gap">
        <a class="btn btn-primary btn-block" data-confirm="Are you sure? You still have mandatory tasks to do on the projects &quot;0x12. JavaScript - Warm up&quot;, &quot;0x01. Share your knowledge - IoT&quot;, &quot;0x06. A tweet a day keeps the @julienbarbier42 away&quot;, you really should focus on those first." href="/projects/303/unlock_optionals">Done with the mandatory tasks? Unlock 4 advanced tasks now!</a>
    </p>







  </div>
</div>