from fabric import task


# Home
#       https://www.fabfile.org/installing.html
#       https://docs.fabfile.org/en/stable/getting-started.html
#       https://docs.fabfile.org/en/stable/api/connection.html#connect-kwargs-arg
#
# Examples:
#       https://jenyay.net/Programming/Fabric#advanced
#


@task
def task1(c):
    print("Task 1")

@task
def task2(c):
    print ("Task 2")


def backup ():
    print('Run backup...')
    print('Ok')


@task
def deploy (c):
    """
    The example of command description
    """
    print('Run deploy...')
    c.run('uname -s', pty=True)
    print('Ok')

