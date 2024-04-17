import chatpdb


def sample_trace_function():
    x = 3
    y = "hello"
    z = [1, 2, 3]
    chatpdb.set_trace()
    print(x, y, z)


@chatpdb.iex
def sample_iex_function():
    raise


@chatpdb.cex
def sample_cex_function():
    raise


def sample_with_function():
    with chatpdb.launch_chatpdb_on_exception():
        raise


if __name__ == "__main__":
    sample_trace_function()
    sample_iex_function()
    sample_with_function()
