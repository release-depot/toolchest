from toolchest.filesystem.git import generate_gitreview


def test_gen_single_gitreview(tmp_path):
    """
    GIVEN a list of .gitreview fields including a defaultrebase value
    WHEN generate_gitreview is called
    THEN a .gitreview file is written with the specified fields
    AND the given defaultrebase value is written to the file
    """
    path = tmp_path
    host = "random_host_str"
    host_port = "1234"
    project = "test_project"
    branch = "test_branch_name"
    remote = "test_remote"
    rebase = 0

    generate_gitreview(path,
                       project,
                       host,
                       host_port,
                       branch,
                       remote,
                       rebase)

    with open(f"{path}/.gitreview", "r") as file_opened:
        correct_output = [
            "[gerrit]\n",
            "host=random_host_str\n",
            "port=1234\n",
            "project=test_project.git\n",
            "defaultbranch=test_branch_name\n",
            "defaultremote=test_remote\n",
            "defaultrebase=0\n"
        ]
        for line in correct_output:
            assert line == file_opened.readline()


def test_gen_single_default_rebase_gitreview(tmp_path):
    """
    GIVEN a list of .gitreview fields without defaultrebase given
    WHEN generate_gitreview is called
    THEN a .gitreview file is written with the specified fields
    AND defaultrebase is given a value of 1 in the .gitreview file
    """
    path = tmp_path
    host = "random_host_str"
    host_port = "1234"
    project = "test_project"
    branch = "test_branch_name"
    remote = "test_remote"

    generate_gitreview(path,
                       project,
                       host,
                       host_port,
                       branch,
                       remote)

    with open(f"{path}/.gitreview", "r") as file_opened:
        correct_output = [
            "[gerrit]\n",
            "host=random_host_str\n",
            "port=1234\n",
            "project=test_project.git\n",
            "defaultbranch=test_branch_name\n",
            "defaultremote=test_remote\n",
            "defaultrebase=1\n"
        ]
        for line in correct_output:
            assert line == file_opened.readline()
