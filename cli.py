# Despite the fact that Unix shells are very similar, there are still some differences between them.
# In order to ensure that what you learn here is as universally applicable as possible, we'll be focusing on learning portable
# commands, by following a set of standards for Unix-like operating systems called POSIX (pronounced pahz-icks as in positive).
# This way, we'll actually be studying several shells simultaneously, while exemplifying with Bash. We'll let you know when a command
# isn't POSIX compliant.
history
!!
clear
exit
pwd
ls
ls prize_winners
ls -A prize_winners
ls -Ahl
cd /home/dq/prize_winners
cd /home
answer false true false
cd /home
ls dq
ls -al dq/prize_winners
mkdir /home/dq/brets
mkdir dir2 dir3 dir5
rmdir brets
mkdir brats
rmdir dir2 dir3 dir5
cp augustus violet veruca tv brats
cp /home/dq/prize_winners/.mike /home/dq/prize_winners/mike
cp -R prize_winners/ brats/
cd
rm augustus violet veruca tv
rm -R prize_winners
mv /home/dq/brats/prize_winners/mike /home/dq/brats #moving a file
mv /home/dq/brats/prize_winners/.mike /home/dq/brats/prize_winners/Mike #rename a file
# The shell gives us a way to specify groups of files by creating patterns to match filenames. In this mission we will be learning
# about this feature.
# The patterns we create to match filenames are called glob patterns. This works in a similar way to regular expressions,
# which you learned earlier, only the characters used and their roles are a bit different. Glob patterns are built from
# special characters called wildcards, and from regular characters.
cd ~/brats
ls v* #files starrting with v
ls ???? #files with 4 letter long length
cp augustus a\*
cp tv 't?'
ls 'a*' 't?'
ls *[!aiueo]
ls *[[:alnum:]] #files that end with either number or letters
cd /home/dq/practice/wildcards
ls
mkdir html_files archive data
mv *l html_files
mv 201[!9]* archive
mv 2019* data
find / -name '*.b64'#finding the filename
mv /sqlite-autoconf-3210000/tea/win/you_found_it.b64 ~ #moving the file to home dir


whoami
id #id of who is logged in
groups
cd
ls -l #listing the non-hidden files in long format
cd / #enter the root directory
ls -l
mkdir oops
cd root




The permissions argument can have many different looks. On this screen, we will explore the symbolic ones.
In the symbolic notation, this argument can be divided into three components:

Scope: owner/user (u), group (g), others (o), all (a – this references all scopes simultaneously)
Operator: add (+), remove (-), set (=)
Mode: read (r), write (w), execute (x)

With this context, we can now rewrite the command above as:

chmod [ugoa][+-=][rwx] files

It is now worth quoting from the documentation:

The operator + causes the selected file mode bits to be added to the existing file mode bits of each file;
- causes them to be removed; and = causes them to be added and causes unmentioned bits to be removed.

In the table below, you can find a few usage examples. The name of the file which the commands act upon is omitted.
For an explicit example, you can read the first row as: my_file had permissions rw-rw-r--, before running chmod u+x my_file,
and it ended up with permissions rwxrw-r-- after running it.

Before command	 Command	    After command
rw-rw-r--	     chmod u+x
rwxrw-r--
rw-rw-r--	     chmod g-w	      rw-r--r--
rwxrwxr--	     chmod o=rx	      rwxrwxr-x
Doesn't matter	 chmod a=x	      --x--x--x

We can also simultaneously set permissions for several scopes. To set all permissions for the owner,
read and execute permissions for the group, and read permissions for all other users, we can run chmod u=rwx,g=rx,o=r my_file.
The permissions argument is comma-separated — including spaces will cause an error. The order of the modes doesn't matter.
Here are a few more examples:

Before command	         Command	        After command
Doesn't matter	     chmod g=rx,u=wrx,o=r	    rwxr-xr--
r-xr-----	         chmod g+x,o+r	            r-xr-xr--
r-xr-xr--	         chmod u+w,g-x,o-r	        rwxr-----
Doesn't matter	     chmod g=xrw,o=xwr,u=rwx	rwxrwxrwx
Doesn't matter	     chmod a=rwx	            rwxrwxrwx

The commands in the last two rows are equivalent, they do exactly the same thing.

chmod is very flexible, there are many syntax variations that make it work. We've looked at enough of them to allow us to do
anything we want. Before we move on to the instructions, we're going to briefly mention a couple more features of this command:

As with most commands we've learned, we can use chmod on more than one file and even use wildcards.
For instance, chmod g+r * would ensure that all files have the read mode enabled for the owner group.
It also allows us to copy permissions from one scope to another. Let's say we want to give the group scope of my_file the same
permissions that the user scope has. This can be achieved with chmod g=u my_file. We just use the source scope in place of the
permissions.

chmod a+rwx mistery_file
chmod g+wx,o+w Trash
chmod g+x config_file_1
chmod g+x,o=r config_file_2
chmod a=rwx,o-x d*



stat /home/dq/Trash

# octal notations
---:0 (no permissions)
--x:1 (execute only permission)
-w-:2 (write only permissions)
-wx:3 (write and execute permissions)
r--:4 (read only permissions)
r-x:5 (read and execute permissions)
rw-:6 (read and write permissions)
rwx:7 (read, write, and execute permissions)

We now see where 644 in 0644 comes from. The first digit, in this case 0, concerns the special permissions (s, S, t, T) that we l
earned about earlier in the mission. The remaining ones pertain, in order, to:

The permissions of the owner: rw-:4+2+0 = 6
The permissions of the group: r--:4+0+0:4
The permissions of others: r--:4.


cd ~/rg_data
head -n 3 Education
tail -n +2 Arts

column characters
column -s":" -t characters


cd ~/rg_data
shuf 'Law & Public Policy'
shuf -n 5 Engineering

cd ~/files
ls -l
file *

# This skill is called text processing. Here are some tasks that fall under this concept:
#
# Reformatting the text
# Extracting specific parts of the text
# Modifying the text
# You already learned how to do some text processing in Python when you learned about regular expressions and other techniques to
# deal with strings.
# One of the advantages of the shell over Python is since commands interact more intimately with the filesystem, it tends to
# be faster for tasks directly concerning input and output of files. It's very common to use the shell to prune a text file to
# obtain only the information that is relevant to us, and then work on it using Python.
# In this mission we're going to be learning how to use some of the shell's most popular commands to work with text files.
# A couple of examples are sort and grep. In a later course we'll learn about two very powerful text-processing command line tools:
# AWK and sed.
cd ~/rg_data
cat *

cat Interdisciplinary
tac Interdisciplinary

cd ~/rg_data
cat Interdisciplinary
sort Interdisciplinary
sort -ru Interdisciplinary "Law & Public Policy"

sort -t":" -k3,3 characters_no_header
sort -t":" -k4,4g characters_no_header

sort -t":" -k3,3 -k4,4gr characters_no_header

grep -v '9$' characters_no_header
cd rg_data
grep -i ',Math' *

cut -d"," -f2,4-6 "Computers & Mathematics"

echo "This is a command line interface."

grep -hi ',Math' /home/dq/rg_data/* >/home/dq/math_data
help echo >/home/dq/echo_help

head -n 1 /home/dq/rg_data/Computers\ \&\ Mathematics >>math_dataset
grep -hi ',Math' /home/dq/rg_data/* >>math_dataset

cut -d"," -f2,1-2,5 "math_dataset"

touch empty_file_1 empty_file_2 #creating empty files

# We can connect the output of command1 to the input of command2 by running command1 | command2. The vertical bar (|) is
# called a pipe and it is responsible for "piping" the output of the first command into the input of the second command.

zen | grep "better"
cd ~/rg_data
sort -u * | wc -l
echo "This is just going to disappear." >/dev/null

find / -name 'dq' 2>stderr
ls /home/inexistent 2>>stderr

ls /dev/null /home/inexistent >all_output 2>all_output
cat all_output #errors

ls /dev/null /home/inexistent >all_output_v2 2>&1
echo "The first clue is in an image you encountered in this course." >/dev/null 2>&1

ls /dev/null /home/inexistent 2>&1 1>redirection_order
ls /dev/null /home/inexistent >order_verification
diff -y redirection_order order_verification

sort -u >sorted_stdin
a
i
u
e
o
cat sorted_stdin

tr [:lower:] [:upper:] <sorted_stdin
tr [:lower:] [:upper:] <sorted_stdin >mad_vowels
