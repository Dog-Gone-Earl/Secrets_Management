# Dog-Gone-Earl/Secrets_Management

## What this VM does
### Datadog Mysql Connection with Secrets Management

<li>Live example of using Secrets Management with the Agent</li>
<li>Mysql Database will be created</li>
<li>Datadog Agent will be installed on Sandbox</li>
<li>Agent will collect <code>username/password</code> from Python executable for Mysql Integration <code>YAML</code> file</li>

![image](https://github.com/Dog-Gone-Earl/Secrets_Management/assets/107069502/b6c0f7c6-d909-43cb-82db-fd1ef7dcf35e)


<pic of Mysql yaml config>
  
<Show datadog-agent secret command output>
  
<show Agent status showing config>
  
## VM type: Linux Jammy

## Special Instructions

### Run Command:
<pre>
git clone https://github.com/Dog-Gone-Earl/Secrets_Management.git 
cd Secrets_Management
./run.sh up
</pre>
  
## If you receive a permissions error:
<pre>chmod 770 Secrets_Management/run.sh</pre>

## SSH into Sandbox
<pre>./run.sh ssh</pre>
  
### Confirm Secrets Being Used:
<pre>
sudo datadog-agent secret</pre>

## Secrets Managaement Documentation
  <li><link>https://docs.datadoghq.com/agent/guide/secrets-management/?tab=linux#pagetitle</link></li>
