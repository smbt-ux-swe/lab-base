"""
Test Suite for Password Security Tool

Run this file to check if your implementation is correct:
    python test_password_tool.py
"""

from password_tool import check_password_strength, generate_password
import string


def test_basic_scoring():
    """Test 1: Basic password scoring"""
    print("Test 1: Basic scoring... ", end="")
    
    result = check_password_strength("Hello123!")
    
    assert result["score"] >= 70, f"Expected score >= 70, got {result['score']}"
    assert result["strength"] == "Strong", f"Expected 'Strong', got {result['strength']}"
    assert "password" in result, "Missing 'password' key in result"
    assert "feedback" in result, "Missing 'feedback' key in result"
    
    print("✓ PASS")


def test_weak_password():
    """Test 2: Weak password detection"""
    print("Test 2: Weak password detection... ", end="")
    
    result = check_password_strength("pass")
    
    assert result["score"] < 40, f"Expected score < 40 for weak password, got {result['score']}"
    assert result["strength"] == "Weak", f"Expected 'Weak', got {result['strength']}"
    
    print("✓ PASS")


def test_common_password():
    """Test 3: Common password detection"""
    print("Test 3: Common password detection... ", end="")
    
    result = check_password_strength("password")
    
    # Should lose points for being common
    assert result["score"] < 50, f"Common password should score low, got {result['score']}"
    
    print("✓ PASS")


def test_strong_password():
    """Test 4: Strong password detection"""
    print("Test 4: Strong password detection... ", end="")
    
    result = check_password_strength("MyP@ssw0rd2024!")
    
    assert result["score"] >= 70, f"Expected strong password score >= 70, got {result['score']}"
    assert result["strength"] in ["Strong", "Very Strong"], f"Expected strong rating, got {result['strength']}"
    
    print("✓ PASS")


def test_generator_length():
    """Test 5: Generator produces correct length"""
    print("Test 5: Generator length... ", end="")
    
    pwd = generate_password(10, False)
    assert len(pwd) == 10, f"Expected length 10, got {len(pwd)}"
    
    pwd = generate_password(15, True)
    assert len(pwd) == 15, f"Expected length 15, got {len(pwd)}"
    
    # Test minimum length
    pwd = generate_password(5, False)
    assert len(pwd) >= 8, f"Expected minimum length 8, got {len(pwd)}"
    
    print("✓ PASS")


def test_generator_requirements():
    """Test 6: Generator includes all required character types"""
    print("Test 6: Generator character types... ", end="")
    
    # Test without special chars
    pwd = generate_password(12, False)
    
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    
    assert has_upper, "Generated password missing uppercase letter"
    assert has_lower, "Generated password missing lowercase letter"
    assert has_digit, "Generated password missing digit"
    
    # Test with special chars
    pwd = generate_password(12, True)
    has_special = any(c in string.punctuation for c in pwd)
    assert has_special, "Generated password missing special character when use_special=True"
    
    print("✓ PASS")


def test_generator_strength():
    """Test 7: Generated passwords are strong"""
    print("Test 7: Generated passwords are strong... ", end="")
    
    # Generate 5 passwords and check they're all strong
    for _ in range(5):
        pwd = generate_password(12, True)
        result = check_password_strength(pwd)
        assert result["score"] >= 70, f"Generated password '{pwd}' only scored {result['score']}"
    
    print("✓ PASS")


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("RUNNING TEST SUITE")
    print("=" * 60 + "\n")
    
    tests = [
        test_basic_scoring,
        test_weak_password,
        test_common_password,
        test_strong_password,
        test_generator_length,
        test_generator_requirements,
        test_generator_strength
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ FAIL - {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR - {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60 + "\n")
    
    if failed == 0:
        print("🎉 All tests passed! Great work!")
        print("Your implementation is correct.\n")
    else:
        print("⚠️  Some tests failed. Keep working on your implementation.\n")


if __name__ == "__main__":
    try:
        run_all_tests()
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        print("Make sure you've implemented both functions in password_tool.py\n")