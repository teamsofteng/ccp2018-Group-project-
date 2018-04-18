

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class CourseReview {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	  System.setProperty("webdriver.chrome.driver",//
			  "/Users/owner/Desktop/chromedriver.exe");
	  driver = new ChromeDriver();
    
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testCourseReview() throws Exception {
    driver.get("http://ec2-35-173-183-216.compute-1.amazonaws.com/");
    driver.findElement(By.linkText("Course Review")).click();
    driver.findElement(By.id("id_courseID")).click();
    driver.findElement(By.id("id_courseID")).clear();
    driver.findElement(By.id("id_courseID")).sendKeys("CIST 2901");
    driver.findElement(By.id("id_overallNode")).click();
    driver.findElement(By.id("id_overallNode")).clear();
    driver.findElement(By.id("id_overallNode")).sendKeys("30");
    driver.findElement(By.id("id_connCourseID")).clear();
    driver.findElement(By.id("id_connCourseID")).sendKeys("CIST 4900");
    driver.findElement(By.id("id_difficultyNode")).clear();
    driver.findElement(By.id("id_difficultyNode")).sendKeys("60");
    driver.findElement(By.id("id_cohesionNode")).clear();
    driver.findElement(By.id("id_cohesionNode")).sendKeys("30");
    Thread.sleep(3000);
    driver.findElement(By.xpath("//button[@type='submit']")).click();
    Thread.sleep(3000);
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
