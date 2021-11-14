use pyo3::prelude::*;

#[pymodule]
fn allow_threads(_: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(test, m)?)?;
    Ok(())
}

#[pyfunction]
fn test(py: Python) {
    py.allow_threads(|| {
        let gil = Python::acquire_gil();
        let _ = gil.python();
    })
}
